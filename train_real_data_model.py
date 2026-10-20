import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, roc_auc_score, confusion_matrix
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import IsolationForest
import xgboost as xgb
import json
import os

print("=" * 70)
print("PELATIHAN MODEL AI VERIKLAIM BERBASIS DATA RIIL BPJS FKRTL 2024")
print("=" * 70)

csv_path = r"D:\Badra\project\Alur_matematika\Marketing_Aqila\bpjs\real_fkrtl_sample_50k.csv"
model_out_path = r"D:\Badra\project\Alur_matematika\Marketing_Aqila\bpjs\real_veriklaim_model.joblib"
stats_out_path = r"D:\Badra\project\Alur_matematika\Marketing_Aqila\bpjs\real_veriklaim_stats.json"

# 1. Load Data
df = pd.read_csv(csv_path)
print(f"Loaded {len(df):,} baris data klaim nyata dari: {csv_path}")

# 2. Extract & Clean Features
print("\nMelakukan Feature Engineering...")

def parse_severity(val):
    s = str(val).lower()
    if 'berat' in s or 'keparahan 3' in s or '-iii' in s:
        return 3
    elif 'sedang' in s or 'keparahan 2' in s or '-ii' in s:
        return 2
    elif 'ringan' in s or 'keparahan 1' in s or '-i' in s:
        return 1
    return 0

df['SEVERITY_NUM'] = df['FKL23'].apply(parse_severity)
df['IS_RITL'] = (df['FKL10'] == 'RITL').astype(int)
df['LOS_HARI'] = df['LOS_HARI'].fillna(0).astype(int)

# Financial variables
df['TARIF_TAGIH'] = df['FKL47'].fillna(0).astype(float)
df['TARIF_VERIFIKASI'] = df['FKL48'].fillna(0).astype(float)
df['SELISIH_DISPUTE'] = (df['TARIF_TAGIH'] - df['TARIF_VERIFIKASI']).clip(lower=0)
df['RATIO_TAGIH_VERIF'] = df['TARIF_TAGIH'] / (df['TARIF_VERIFIKASI'] + 1.0)

# Specialized risk indicators
df['IS_ZERO_LOS_INPATIENT'] = ((df['IS_RITL'] == 1) & (df['LOS_HARI'] == 0)).astype(int)
df['IS_SEV3_SHORT_STAY'] = ((df['SEVERITY_NUM'] == 3) & (df['LOS_HARI'] <= 1)).astype(int)
df['LOS_PER_SEVERITY'] = df['LOS_HARI'] / (df['SEVERITY_NUM'] + 0.1)

# 3. Formulate Ground Truth Label on Real BPJS Data
def assign_fraud_category(row):
    if row['SELISIH_DISPUTE'] > 0:
        return 'DISPUTED_CLAIM'
    elif row['IS_SEV3_SHORT_STAY'] == 1 and row['TARIF_TAGIH'] > 5000000:
        return 'UPCODING'
    elif row['IS_ZERO_LOS_INPATIENT'] == 1 and row['TARIF_TAGIH'] > 1500000:
        return 'PHANTOM_BILLING'
    else:
        return 'NORMAL'

df['FRAUD_CATEGORY'] = df.apply(assign_fraud_category, axis=1)
df['IS_ANOMALOUS'] = (df['FRAUD_CATEGORY'] != 'NORMAL').astype(int)

counts = df['FRAUD_CATEGORY'].value_counts()
print("\nDistribusi Kategori Kasus pada Data Real 50.000 Klaim:")
for cat, cnt in counts.items():
    print(f"  - {cat:16s}: {cnt:,} kasus ({cnt/len(df)*100:.2f}%)")

# 4. Encoding
cat_cols = ['FKL09', 'FKL10', 'FKL12', 'FKL17A', 'FKL19', 'FKL31']
encoders = {}
for col in cat_cols:
    le = LabelEncoder()
    df[col + '_ENC'] = le.fit_transform(df[col].astype(str))
    encoders[col] = le

feature_cols = [
    'IS_RITL', 'LOS_HARI', 'SEVERITY_NUM', 'TARIF_TAGIH', 'TARIF_VERIFIKASI',
    'RATIO_TAGIH_VERIF', 'IS_ZERO_LOS_INPATIENT', 'IS_SEV3_SHORT_STAY',
    'LOS_PER_SEVERITY', 'FKL09_ENC', 'FKL10_ENC', 'FKL12_ENC', 'FKL17A_ENC',
    'FKL19_ENC', 'FKL31_ENC'
]

X = df[feature_cols]
y_bin = df['IS_ANOMALOUS']

target_le = LabelEncoder()
y_multi = target_le.fit_transform(df['FRAUD_CATEGORY'])
encoders['FRAUD_CATEGORY'] = target_le

# 5. Train-Test Split (80% Train, 20% Test)
X_train, X_test, y_train_bin, y_test_bin, y_train_mul, y_test_mul = train_test_split(
    X, y_bin, y_multi, test_size=0.20, random_state=42, stratify=y_multi
)

# 6. Train Model 1: XGBoost Anomaly Detector
print("\nMelatih Model 1: XGBoost Anomaly Classifier...")
scale_pos = (len(y_train_bin) - sum(y_train_bin)) / (sum(y_train_bin) + 1)
model_xgb_bin = xgb.XGBClassifier(
    n_estimators=100,
    max_depth=5,
    learning_rate=0.08,
    scale_pos_weight=scale_pos,
    eval_metric='logloss',
    random_state=42
)
model_xgb_bin.fit(X_train, y_train_bin)

y_pred_bin = model_xgb_bin.predict(X_test)
y_prob_bin = model_xgb_bin.predict_proba(X_test)[:, 1]
roc_auc = roc_auc_score(y_test_bin, y_prob_bin)

print(f"-> ROC-AUC Score: {roc_auc:.4f}")
print("Classification Report (Binary Anomaly Detection):")
print(classification_report(y_test_bin, y_pred_bin, target_names=['Normal', 'Anomali/Dispute']))

# 7. Train Model 2: Multi-Class Fraud Typology
print("\nMelatih Model 2: Multi-Class Typology Classifier...")
model_xgb_mul = xgb.XGBClassifier(
    n_estimators=120,
    max_depth=6,
    learning_rate=0.08,
    objective='multi:softprob',
    num_class=len(target_le.classes_),
    eval_metric='mlogloss',
    random_state=42
)
model_xgb_mul.fit(X_train, y_train_mul)

y_pred_mul = model_xgb_mul.predict(X_test)
print("Classification Report (Multi-Class):")
print(classification_report(y_test_mul, y_pred_mul, target_names=target_le.classes_))

# 8. Feature Importance
imp = dict(zip(feature_cols, model_xgb_bin.feature_importances_))
sorted_imp = sorted(imp.items(), key=lambda x: x[1], reverse=True)
print("\nTop 6 Fitur Penentu Anomali (Feature Importance):")
for f, v in sorted_imp[:6]:
    print(f"  - {f:22s}: {v*100:.2f}%")

# 9. Train Model 3: Unsupervised Outlier Detector (Isolation Forest)
print("\nMelatih Model 3: Isolation Forest (Zero-Day Outlier Detection)...")
iso_forest = IsolationForest(contamination=0.01, random_state=42, n_estimators=100)
iso_forest.fit(X_train)

# 10. Save Model Artifacts
artifacts = {
    'binary_model': model_xgb_bin,
    'multi_model': model_xgb_mul,
    'isolation_forest': iso_forest,
    'encoders': encoders,
    'feature_cols': feature_cols,
    'classes': target_le.classes_.tolist()
}

joblib.dump(artifacts, model_out_path)
print(f"\nModel tersimpan di: {model_out_path}")

# 11. Run Real Inference Demonstrations on 4 Real Cases
print("\n" + "=" * 70)
print("CONTOH INFERENSI PADA KLAIM NYATA DARI RUMAH SAKIT")
print("=" * 70)

for cat in target_le.classes_:
    sub = df[df['FRAUD_CATEGORY'] == cat].iloc[0]
    sub_X = X.iloc[[sub.name]]
    p_bin = model_xgb_bin.predict(sub_X)[0]
    p_prob = model_xgb_bin.predict_proba(sub_X)[0][1]
    p_type = target_le.inverse_transform(model_xgb_mul.predict(sub_X))[0]
    
    print(f"\nNo Kunjungan : {sub['FKL02']}")
    print(f"Tipe RS      : {sub['FKL09']} | Pelayanan: {sub['FKL10']}")
    print(f"Diagnosa     : {sub['FKL18A']} (ICD-10: {sub['FKL17A']})")
    print(f"INA-CBG      : {sub['FKL19']} - {sub['FKL19A']}")
    print(f"Keparahan    : {sub['FKL23']} (Level {sub['SEVERITY_NUM']}) | LOS: {sub['LOS_HARI']} Hari")
    print(f"Biaya Tagih  : Rp {sub['TARIF_TAGIH']:,} | Tarif Verifikasi: Rp {sub['TARIF_VERIFIKASI']:,}")
    if sub['SELISIH_DISPUTE'] > 0:
        print(f"Jejak BPJS   : DIPOTONG VERIFIKATOR SEBESAR Rp {sub['SELISIH_DISPUTE']:,}!")
    print(f"Hasil AI     : {'[TERDETEKSI ANOMALI]' if p_bin else '[KLAIM WAJAR]'} -> Tipe: {p_type} (Keyakinan: {p_prob*100:.1f}%)")

# Save summary stats
summary = {
    "model_name": "VeriKlaim XGBoost & Isolation Forest (Real BPJS 2024)",
    "training_samples": len(X_train),
    "test_samples": len(X_test),
    "roc_auc_score": round(float(roc_auc), 4),
    "class_counts": {k: int(v) for k, v in counts.items()},
    "top_features": {k: round(float(v)*100, 2) for k, v in sorted_imp[:6]}
}
with open(stats_out_path, "w", encoding="utf-8") as f:
    json.dump(summary, f, indent=2)

print("\nPelatihan selesai dengan sukses!")
