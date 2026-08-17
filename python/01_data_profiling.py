# Import libraries
import pandas as pd
import numpy as np
from pathlib import Path


# find all CSV files(data inventory) in the data folder
data_path = Path("C:/Projects/Olist E-Commerce Business Intelligence & Customer Analytics Platform/data/Raw")
csv_files = list(data_path.glob("*.csv"))
#print(csv_files)
for file in csv_files:
    print(f"Profiling {file.name}")

#Load all datasets
Datasets = {}
for file in csv_files:
    name = file.stem
    Datasets[name] = pd.read_csv(file)
    print(Datasets.keys())

#Profile the size of every table
table_summary = []
for name, df in Datasets.items():
    table_summary.append({
        "table": name,
        "rows": df.shape[0],
        "columns": df.shape[1]
    })
table_summary = pd.DataFrame(table_summary)

table_summary

# Profile the columns of every table
column_summary = []
for name, df in Datasets.items():
    for col in df.columns:
        column_summary.append({
            "table": name,
            "column": col,
            "dtype": df[col].dtype,
             "missing": df[col].isna().sum(),
            "unique": df[col].nunique()
        })

column_summary = pd.DataFrame(column_summary)

column_summary
