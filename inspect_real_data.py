import pandas as pd
import json

fkrtl_path = r"D:\Badra\project\Alur_matematika\Marketing_Aqila\bpjs\Data sampel 2015-2024 (1)\2025\Data Sampel Reguler Edisi 2025\data\202403_fkrtl.dta"

print(f"Reading metadata and first few rows from: {fkrtl_path}")

# Read using StataReader for metadata without loading full 629MB into RAM
with pd.io.stata.StataReader(fkrtl_path) as reader:
    var_labels = reader.variable_labels()
    val_labels = reader.value_labels()
    print(f"\n--- Total Columns: {len(var_labels)} ---")
    for col, label in var_labels.items():
        print(f"  {col:15s} : {label}")
        
    # Read first 5 rows
    df_sample = reader.read(nrows=5)
    print("\n--- First 5 Rows ---")
    print(df_sample.to_string())

# Also check kepesertaan columns
kep_path = r"D:\Badra\project\Alur_matematika\Marketing_Aqila\bpjs\Data sampel 2015-2024 (1)\2025\Data Sampel Reguler Edisi 2025\data\2015202401_kepesertaan.dta"
print(f"\nReading metadata from: {kep_path}")
with pd.io.stata.StataReader(kep_path) as reader:
    var_labels_kep = reader.variable_labels()
    print(f"--- Kepesertaan Columns ({len(var_labels_kep)}): ---")
    for col, label in var_labels_kep.items():
        print(f"  {col:15s} : {label}")
