import csv
import random
from datetime import datetime, timedelta

# Seed for reproducibility
random.seed(42)

TOTAL_RECORDS = 10000

# Base Data Definitions
HOSPITALS = [
    {"id": f"FAS-{i:03d}", "tipe": random.choice(["RS Tipe A", "RS Tipe B", "RS Tipe C", "RS Tipe D"]), "prov": random.choice(["DKI Jakarta", "Jawa Barat", "Jawa Timur", "Sumatera Utara", "Kalimantan Barat"])}
    for i in range(1, 51)
]

PATIENTS = [
    {
        "id": f"PST-{i:05d}",
        "gender": random.choice(["L", "P"]),
        "age": random.randint(18, 78),
        "segmen": random.choice(["PBI APBN", "PBI APBD", "PPU", "PBPU"])
    }
    for i in range(1, 3001)
]

CLINICAL_PROFILES = [
    {
        "diag_utama": "E11.9", "diag_nama": "Diabetes Melitus Tipe 2 Tanpa Komplikasi",
        "diag_sekunder": ["I10", "E78.5", "-"],
        "proc": ["90.59", "-"], # Lab blood exam
        "cbg_base": "E-4-10", "cbg_nama": "GANGGUAN DIABETES",
        "tarif": {1: 3200000, 2: 5800000, 3: 11200000},
        "los_range": (2, 4)
    },
    {
        "diag_utama": "K35.8", "diag_nama": "Apendisitis Akut Lainnya",
        "diag_sekunder": ["R10.4", "K52.9", "-"],
        "proc": ["47.09"], # Appendectomy
        "cbg_base": "K-1-12", "cbg_nama": "PROSEDUR APENDIKS",
        "tarif": {1: 7500000, 2: 12800000, 3: 21500000},
        "los_range": (3, 6)
    },
    {
        "diag_utama": "J18.9", "diag_nama": "Pneumonia Tidak Spesifik",
        "diag_sekunder": ["J44.9", "R05", "-"],
        "proc": ["87.44", "96.71", "-"], # Chest xray, mechanical ventilation
        "cbg_base": "J-4-16", "cbg_nama": "INFEKSI SALURAN PERNAPASAN",
        "tarif": {1: 4800000, 2: 8900000, 3: 17400000},
        "los_range": (3, 7)
    },
    {
        "diag_utama": "I50.9", "diag_nama": "Gagal Jantung Kongestif",
        "diag_sekunder": ["I10", "I25.1", "N18.9"],
        "proc": ["88.72", "89.52", "-"], # Echocardiography, ECG
        "cbg_base": "I-4-12", "cbg_nama": "GAGAL JANTUNG",
        "tarif": {1: 5200000, 2: 9800000, 3: 19600000},
        "los_range": (4, 8)
    },
    {
        "diag_utama": "H25.9", "diag_nama": "Katarak Senilis",
        "diag_sekunder": ["-"],
        "proc": ["13.41"], # Phacoemulsification
        "cbg_base": "H-1-30", "cbg_nama": "PROSEDUR LENSA MATA",
        "tarif": {1: 5100000, 2: 7800000, 3: 12000000},
        "los_range": (1, 2)
    },
    {
        "diag_utama": "O82.0", "diag_nama": "Persalinan Sesar Elektif",
        "diag_sekunder": ["O68.0", "O34.2", "-"],
        "proc": ["74.1"], # Caesarean Section
        "cbg_base": "O-1-20", "cbg_nama": "BEDAH SESAR",
        "tarif": {1: 6800000, 2: 11500000, 3: 18900000},
        "los_range": (3, 5)
    },
    {
        "diag_utama": "N18.5", "diag_nama": "Penyakit Ginjal Kronis Stadium 5",
        "diag_sekunder": ["I10", "E11.2"],
        "proc": ["39.95"], # Hemodialysis
        "cbg_base": "N-3-10", "cbg_nama": "HEMODIALISIS KRONIS",
        "tarif": {1: 1100000, 2: 1800000, 3: 3200000},
        "los_range": (1, 1)
    }
]

start_date = datetime(2025, 1, 1)

rows = []
sep_counter = 1

for i in range(TOTAL_RECORDS):
    patient = random.choice(PATIENTS)
    hospital = random.choice(HOSPITALS)
    profile = random.choice(CLINICAL_PROFILES)
    
    # Random admission date over 1 year
    adm_date = start_date + timedelta(days=random.randint(0, 360))
    nomor_sep = f"SEP-{hospital['id']}-{adm_date.strftime('%Y%m%d')}-{sep_counter:05d}"
    sep_counter += 1
    
    # Decide Fraud Type
    # 82% Normal, 10% Upcoding, 5% Unbundling, 3% Phantom
    rand_val = random.random()
    
    if rand_val < 0.82:
        # NORMAL
        fraud_type = "NORMAL"
        is_fraud = 0
        severity = random.choices([1, 2, 3], weights=[0.65, 0.25, 0.10])[0]
        cbg_code = f"{profile['cbg_base']}-{['I','II','III'][severity-1]}"
        los = random.randint(profile['los_range'][0], profile['los_range'][1])
        dis_date = adm_date + timedelta(days=los)
        tarif_cbg = profile['tarif'][severity]
        # Real hospital cost typically within +- 15% of CBG tariff
        biaya_riil = int(tarif_cbg * random.uniform(0.85, 1.15))
        proc = random.choice(profile['proc'])
        diag_sekunder = random.choice(profile['diag_sekunder'])
        fraud_reason = "Klaim wajar dan koheren secara klinis"
        
    elif rand_val < 0.92:
        # UPCODING
        fraud_type = "UPCODING"
        is_fraud = 1
        # Patient only has minor condition, but hospital claims Severity III (Heavy) with high tariff
        severity = 3
        cbg_code = f"{profile['cbg_base']}-III"
        # Actual LOS is very short, uncharacteristic of severity III
        los = random.randint(1, 2)
        dis_date = adm_date + timedelta(days=los)
        tarif_cbg = profile['tarif'][3]
        # Biaya riil RS sebenarnya hanya selevel severity 1
        biaya_riil = int(profile['tarif'][1] * random.uniform(0.70, 0.95))
        proc = "-"  # Prosedur pendukung severity III tidak ditemukan
        diag_sekunder = "R68.89" # Gejala minor palsu untuk melegitimasi severity III
        fraud_reason = "Penggelembungan tingkat keparahan (Severity III) tanpa tindakan medis dan lama rawat yang sesuai"
        
    elif rand_val < 0.97:
        # UNBUNDLING / SPLIT BILLING
        fraud_type = "UNBUNDLING"
        is_fraud = 1
        severity = 1
        cbg_code = f"{profile['cbg_base']}-I"
        los = 1
        dis_date = adm_date + timedelta(days=1)
        tarif_cbg = profile['tarif'][1]
        biaya_riil = int(tarif_cbg * 0.9)
        proc = random.choice(profile['proc'])
        diag_sekunder = "-"
        fraud_reason = "Pemecahan prosedur tunggal menjadi beberapa episode kunjungan terpisah dalam waktu < 48 jam"
        
    else:
        # PHANTOM BILLING
        fraud_type = "PHANTOM_BILLING"
        is_fraud = 1
        severity = random.choice([2, 3])
        cbg_code = f"{profile['cbg_base']}-{['I','II','III'][severity-1]}"
        # LOS 0 days for severe inpatient treatment, or phantom procedure
        los = 0
        dis_date = adm_date # Pulang hari yang sama tapi klaim RITL rawat inap berat
        tarif_cbg = profile['tarif'][severity]
        biaya_riil = 0 # Tidak ada pengeluaran riil farmasi / bedah tercatat
        proc = "99.99"
        diag_sekunder = "Z00.0"
        fraud_reason = "Klaim rawat inap dengan LOS 0 hari dan biaya riil farmasi/tindakan fiktif"

    rows.append({
        "NO_SEP": nomor_sep,
        "ID_PESERTA": patient["id"],
        "USIA": patient["age"],
        "JENIS_KELAMIN": patient["gender"],
        "SEGMEN_PESERTA": patient["segmen"],
        "ID_FASKES": hospital["id"],
        "TIPE_FASKES": hospital["tipe"],
        "PROVINSI_FASKES": hospital["prov"],
        "TGL_MASUK": adm_date.strftime("%Y-%m-%d"),
        "TGL_PULANG": dis_date.strftime("%Y-%m-%d"),
        "LOS_HARI": los,
        "KODE_ICD10_UTAMA": profile["diag_utama"],
        "NAMA_DIAGNOSA": profile["diag_nama"],
        "KODE_ICD10_SEKUNDER": diag_sekunder,
        "KODE_ICD9_PROSEDUR": proc,
        "KODE_INACBG": cbg_code,
        "NAMA_INACBG": profile["cbg_nama"],
        "SEVERITY_LEVEL": severity,
        "BIAYA_RIIL_RS": biaya_riil,
        "TARIF_INACBG": tarif_cbg,
        "SELISIH_BIAYA": tarif_cbg - biaya_riil,
        "IS_FRAUD": is_fraud,
        "FRAUD_TYPE": fraud_type,
        "FRAUD_REASON": fraud_reason
    })

# Save to CSV
csv_path = "d:/Badra/project/Alur_matematika/Marketing_Aqila/bpjs/dataset_sample_fkrtl_bpjs.csv"
fieldnames = list(rows[0].keys())

with open(csv_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Berhasil menghasilkan {len(rows)} baris data sampel FKRTL!")
print(f"File tersimpan di: {csv_path}")

# Quick summary
fraud_counts = {}
for r in rows:
    ft = r["FRAUD_TYPE"]
    fraud_counts[ft] = fraud_counts.get(ft, 0) + 1

print("\nDistribusi Data:")
for k, v in fraud_counts.items():
    print(f"- {k}: {v} baris ({v/len(rows)*100:.1f}%)")
