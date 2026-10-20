import pandas as pd
import json

df = pd.read_csv("d:/Badra/project/Alur_matematika/Marketing_Aqila/bpjs/dataset_sample_fkrtl_bpjs.csv")

total_claims = len(df)
fraud_df = df[df['IS_FRAUD'] == 1]
total_fraud = len(fraud_df)
total_normal = total_claims - total_fraud

total_claim_amount = int(df['TARIF_INACBG'].sum())
total_fraud_saved = int(fraud_df['SELISIH_BIAYA'].apply(lambda x: max(0, x)).sum())

# Breakdown by type
type_counts = df['FRAUD_TYPE'].value_counts().to_dict()
type_savings = {}
for ft in ['UPCODING', 'UNBUNDLING', 'PHANTOM_BILLING']:
    sub = df[df['FRAUD_TYPE'] == ft]
    type_savings[ft] = int(sub['SELISIH_BIAYA'].apply(lambda x: max(0, x)).sum())

# Breakdown by RS Type
rs_type_breakdown = {}
for rs in df['TIPE_FASKES'].unique():
    sub = df[df['TIPE_FASKES'] == rs]
    f_count = len(sub[sub['IS_FRAUD'] == 1])
    rs_type_breakdown[rs] = {
        'total': len(sub),
        'fraud': f_count,
        'fraud_rate': round(f_count / len(sub) * 100, 2)
    }

stats = {
    'total_claims': total_claims,
    'total_fraud': total_fraud,
    'total_normal': total_normal,
    'fraud_rate_pct': round(total_fraud / total_claims * 100, 2),
    'total_claim_amount': total_claim_amount,
    'total_fraud_saved': total_fraud_saved,
    'type_counts': type_counts,
    'type_savings': type_savings,
    'rs_breakdown': rs_type_breakdown
}

with open("d:/Badra/project/Alur_matematika/Marketing_Aqila/bpjs/precomputed_stats.json", "w") as f:
    json.dump(stats, f, indent=2)

print("Precomputed Stats calculated successfully:")
print(f"Total Fraud: {total_fraud} ({stats['fraud_rate_pct']}%)")
print(f"Potensi Dana Diselamatkan: Rp {total_fraud_saved:,}")
