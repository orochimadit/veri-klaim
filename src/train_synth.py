import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, roc_auc_score, confusion_matrix
from sklearn.preprocessing import LabelEncoder
import xgboost as xgb
import json
import os

# 1. Load Dataset
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)
data_path = os.path.join(ROOT_DIR, "data", "dataset_sample_fkrtl_bpjs.csv")
df = pd.read_csv(data_path)
print(f"Loaded {len(df)} records from {data_path}")

# 2. Feature Engineering
print("Performing Feature Engineering...")
df['COST_RATIO'] = df['BIAYA_RIIL_RS'] / (df['TARIF_INACBG'] + 1.0)
df['COST_DIFF'] = df['TARIF_INACBG'] - df['BIAYA_RIIL_RS']
df['LOS_PER_SEVERITY'] = df['LOS_HARI'] / (df['SEVERITY_LEVEL'] + 0.1)
df['HAS_PROCEDURE'] = (df['KODE_ICD9_PROSEDUR'] != '-').astype(int)
df['HAS_COMORBID'] = (df['KODE_ICD10_SEKUNDER'] != '-').astype(int)
df['IS_ZERO_LOS'] = (df['LOS_HARI'] == 0).astype(int)
df['IS_ZERO_REAL_COST'] = (df['BIAYA_RIIL_RS'] == 0).astype(int)

# Encode categorical variables
cat_cols = ['TIPE_FASKES', 'SEGMEN_PESERTA', 'JENIS_KELAMIN', 'NAMA_INACBG', 'KODE_ICD10_UTAMA']
encoders = {}
for col in cat_cols:
    le = LabelEncoder()
    df[col + '_ENC'] = le.fit_transform(df[col].astype(str))
    encoders[col] = le

feature_cols = [
    'USIA', 'JENIS_KELAMIN_ENC', 'SEGMEN_PESERTA_ENC', 'TIPE_FASKES_ENC',
    'LOS_HARI', 'SEVERITY_LEVEL', 'BIAYA_RIIL_RS', 'TARIF_INACBG',
    'COST_RATIO', 'COST_DIFF', 'LOS_PER_SEVERITY', 'HAS_PROCEDURE',
    'HAS_COMORBID', 'IS_ZERO_LOS', 'IS_ZERO_REAL_COST',
    'NAMA_INACBG_ENC', 'KODE_ICD10_UTAMA_ENC'
]

X = df[feature_cols]

# Target 1: Binary Fraud
y_binary = df['IS_FRAUD']

# Target 2: Multi-class Fraud Type
target_encoder = LabelEncoder()
y_multi = target_encoder.fit_transform(df['FRAUD_TYPE'])
encoders['FRAUD_TYPE'] = target_encoder

# 3. Train-Test Split (80% train, 20% test, stratified)
X_train, X_test, y_train_bin, y_test_bin, y_train_mul, y_test_mul = train_test_split(
    X, y_binary, y_multi, test_size=0.20, random_state=42, stratify=y_multi
)

print(f"Train samples: {len(X_train)}, Test samples: {len(X_test)}")

# 4. Train Model 1: Binary Fraud Detector (XGBoost)
print("\n=== Training Model 1: Binary Fraud Detector ===")
bin_model = xgb.XGBClassifier(
    n_estimators=120,
    max_depth=5,
    learning_rate=0.08,
    scale_pos_weight=(len(y_train_bin) - sum(y_train_bin)) / sum(y_train_bin),
    eval_metric='logloss',
    random_state=42
)
bin_model.fit(X_train, y_train_bin)

y_pred_bin = bin_model.predict(X_test)
y_prob_bin = bin_model.predict_proba(X_test)[:, 1]
roc_auc = roc_auc_score(y_test_bin, y_prob_bin)

print(f"ROC-AUC Score: {roc_auc:.4f}")
print("Classification Report (Binary):")
print(classification_report(y_test_bin, y_pred_bin, target_names=['Normal', 'Fraud']))

# 5. Train Model 2: Multi-class Fraud Type Classifier (XGBoost)
print("\n=== Training Model 2: Multi-Class Fraud Type Classifier ===")
multi_model = xgb.XGBClassifier(
    n_estimators=150,
    max_depth=6,
    learning_rate=0.08,
    objective='multi:softprob',
    num_class=len(target_encoder.classes_),
    eval_metric='mlogloss',
    random_state=42
)
multi_model.fit(X_train, y_train_mul)

y_pred_mul = multi_model.predict(X_test)
print("Classification Report (Multi-Class Fraud Type):")
print(classification_report(y_test_mul, y_pred_mul, target_names=target_encoder.classes_))

# 6. Feature Importance Analysis
importance = dict(zip(feature_cols, bin_model.feature_importances_))
sorted_imp = sorted(importance.items(), key=lambda x: x[1], reverse=True)
print("\n=== Top Feature Importances (Binary Detection) ===")
for feat, imp in sorted_imp[:8]:
    print(f"- {feat:20s}: {imp*100:.2f}%")

# 7. Save Model Artifacts
artifacts = {
    'binary_model': bin_model,
    'multi_model': multi_model,
    'encoders': encoders,
    'feature_cols': feature_cols,
    'classes': target_encoder.classes_.tolist()
}

model_save_path = os.path.join(ROOT_DIR, "models", "veriklaim_model.joblib")
joblib.dump(artifacts, model_save_path)
print(f"\nModel berhasil disimpan di: {model_save_path}")

# 8. Test Sample Inference on a Real Claim
print("\n=== Contoh Prediksi Klaim Nyata (Inference Test) ===")
sample_indices = [0, 4, 15, 25] # Mix of samples
for idx in sample_indices:
    raw_sample = df.iloc[idx]
    features = X.iloc[[idx]]
    pred_flag = bin_model.predict(features)[0]
    pred_type = target_encoder.inverse_transform(multi_model.predict(features))[0]
    prob = bin_model.predict_proba(features)[0][1]
    
    print(f"SEP: {raw_sample['NO_SEP']}")
    print(f" Diagnosa   : {raw_sample['NAMA_DIAGNOSA']} ({raw_sample['KODE_ICD10_UTAMA']})")
    print(f" CBG & Lev  : {raw_sample['KODE_INACBG']} (Level {raw_sample['SEVERITY_LEVEL']}) | LOS: {raw_sample['LOS_HARI']} hari")
    print(f" Tarif Klaim: Rp {raw_sample['TARIF_INACBG']:,} | Biaya Riil: Rp {raw_sample['BIAYA_RIIL_RS']:,}")
    print(f" GroundTruth: {raw_sample['FRAUD_TYPE']}")
    print(f" Hasil Model: {'🚨 FRAUD DETECTED' if pred_flag else '✅ NORMAL'} -> Tipe: {pred_type} (Confidence: {prob*100:.1f}%)")
    print("-" * 65)
