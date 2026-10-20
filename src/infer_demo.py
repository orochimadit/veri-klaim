import os
import joblib
import pandas as pd
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)

# Load artifact
model_path = os.path.join(ROOT_DIR, "models", "veriklaim_model.joblib")
artifacts = joblib.load(model_path)

bin_model = artifacts['binary_model']
multi_model = artifacts['multi_model']
encoders = artifacts['encoders']
feature_cols = artifacts['feature_cols']
target_encoder = encoders['FRAUD_TYPE']

# Load dataset
df = pd.read_csv(os.path.join(ROOT_DIR, "data", "dataset_sample_fkrtl_bpjs.csv"))

# Feature Engineering
df['COST_RATIO'] = df['BIAYA_RIIL_RS'] / (df['TARIF_INACBG'] + 1.0)
df['COST_DIFF'] = df['TARIF_INACBG'] - df['BIAYA_RIIL_RS']
df['LOS_PER_SEVERITY'] = df['LOS_HARI'] / (df['SEVERITY_LEVEL'] + 0.1)
df['HAS_PROCEDURE'] = (df['KODE_ICD9_PROSEDUR'] != '-').astype(int)
df['HAS_COMORBID'] = (df['KODE_ICD10_SEKUNDER'] != '-').astype(int)
df['IS_ZERO_LOS'] = (df['LOS_HARI'] == 0).astype(int)
df['IS_ZERO_REAL_COST'] = (df['BIAYA_RIIL_RS'] == 0).astype(int)

for col in ['TIPE_FASKES', 'SEGMEN_PESERTA', 'JENIS_KELAMIN', 'NAMA_INACBG', 'KODE_ICD10_UTAMA']:
    df[col + '_ENC'] = encoders[col].transform(df[col].astype(str))

X = df[feature_cols]

# Select 1 representative sample for each category: NORMAL, UPCODING, UNBUNDLING, PHANTOM_BILLING
samples = []
for ftype in ['NORMAL', 'UPCODING', 'UNBUNDLING', 'PHANTOM_BILLING']:
    sub = df[df['FRAUD_TYPE'] == ftype].iloc[0]
    samples.append(sub)

print("=" * 75)
print("HASIL UJI INFERENSI ENGINE VERIKLAIM (PREDIKSI KLAIM REAL-TIME)")
print("=" * 75)

for s in samples:
    row_idx = s.name
    feat = X.iloc[[row_idx]]
    pred_bin = bin_model.predict(feat)[0]
    pred_prob = bin_model.predict_proba(feat)[0][1]
    pred_type = target_encoder.inverse_transform(multi_model.predict(feat))[0]
    
    status_tag = "[TERDETEKSI FRAUD / ANOMALI]" if pred_bin == 1 else "[KLAIM WAJAR / NORMAL]"
    
    print(f"\nNomor SEP     : {s['NO_SEP']}")
    print(f"Pasien / Faskes : Pasien {s['ID_PESERTA']} (Usia {s['USIA']}) | RS {s['ID_FASKES']} ({s['TIPE_FASKES']})")
    print(f"Diagnosa Medis  : {s['NAMA_DIAGNOSA']} (ICD-10: {s['KODE_ICD10_UTAMA']})")
    print(f"INA-CBG & Lev   : {s['KODE_INACBG']} (Level {s['SEVERITY_LEVEL']}) | Lama Rawat (LOS): {s['LOS_HARI']} Hari")
    print(f"Biaya Riil RS   : Rp {s['BIAYA_RIIL_RS']:,} | Nilai Klaim Diajukan: Rp {s['TARIF_INACBG']:,}")
    print(f"Status Sistem   : {status_tag}")
    print(f"Klasifikasi Tipe: {pred_type} (Tingkat Keyakinan AI: {pred_prob*100:.1f}%)")
    print(f"Alasan Anomali  : {s['FRAUD_REASON']}")
    print("-" * 75)
