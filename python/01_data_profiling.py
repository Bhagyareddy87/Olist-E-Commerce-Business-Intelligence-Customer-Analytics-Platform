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
table_summary.to_csv(
    "C:/Projects/Olist E-Commerce Business Intelligence & Customer Analytics Platform/data/Processed/table_summary.csv",
    index=False
)

# Profile the columns of every table
column_summary = []
for name, df in Datasets.items():
    for col in df.columns:
        column_summary.append({
            "table": name,
            "column": col,
            "dtype": df[col].dtype,
             "missing": df[col].isna().sum(),
             "missing_pct": (df[col].isna().sum() / len(df)) * 100,
            "unique": df[col].nunique()
        })

column_summary = pd.DataFrame(column_summary)

column_summary
column_summary.to_csv(
    "C:/Projects/Olist E-Commerce Business Intelligence & Customer Analytics Platform/data/Processed/column_summary.csv",
    index=False
)

# identify columns with missing values
missing_summary = column_summary[column_summary["missing"] > 0]

missing_summary
missing_summary.to_csv(
    "C:/Projects/Olist E-Commerce Business Intelligence & Customer Analytics Platform/data/Processed/missing_summary.csv",
    index=False
)

# identify duplicate rows in each table
duplicate_summary = []

for name, df in Datasets.items():
    duplicate_summary.append({
        "table": name,
        "duplicate_rows": df.duplicated().sum()
    })

duplicate_summary = pd.DataFrame(duplicate_summary)

duplicate_summary
duplicate_summary.to_csv(
    "C:/Projects/Olist E-Commerce Business Intelligence & Customer Analytics Platform/data/Processed/duplicate_summary.csv",
    index=False
)

# identify columns that are likely to be primary keys (columns ending with "_id")
key_summary = []

for name, df in Datasets.items():
    for col in df.columns:
        if col.endswith("_id"):
            key_summary.append({
                "table": name,
                "column": col,
                "rows": len(df),
                "unique_values": df[col].nunique(),
                "duplicate_values": df[col].duplicated().sum()
            })

key_summary = pd.DataFrame(key_summary)

key_summary
key_summary.to_csv(
    "C:/Projects/Olist E-Commerce Business Intelligence & Customer Analytics Platform/data/Processed/key_summary.csv",
    index=False
)

# identify the date - data type
date_summary = []

for name, df in Datasets.items():
    for col in df.columns:
        if ("date" in col.lower()
                or "timestamp" in col.lower()
                or col.lower().endswith("_at")):
            date_summary.append({
                "table": name,
                "column": col,
                "dtype": df[col].dtype
            })

date_summary = pd.DataFrame(date_summary)

date_summary
date_summary.to_csv(
    "C:/Projects/Olist E-Commerce Business Intelligence & Customer Analytics Platform/data/Processed/date_summary.csv",
    index=False
)

# numeric profiling 
numeric_summary = []

for name, df in Datasets.items():
    numeric_cols = df.select_dtypes(include=np.number).columns

    for col in numeric_cols:
        numeric_summary.append({
            "table": name,
            "column": col,
            "min": df[col].min(),
            "max": df[col].max(),
            "mean": df[col].mean(),
            "median": df[col].median(),
            "std": df[col].std()
        })

numeric_summary = pd.DataFrame(numeric_summary)

numeric_summary
numeric_summary.to_csv(
    "C:/Projects/Olist E-Commerce Business Intelligence & Customer Analytics Platform/data/Processed/numeric_summary.csv",
    index=False
)

# ============================================================
# DATA PROFILING SUMMARY
# ============================================================
#
# Data profiling was performed on all Olist e-commerce datasets
# to understand the structure, completeness, consistency, and
# basic characteristics of the raw data before data cleaning.
#
# Profiling activities completed:
#
# 1. Data Inventory
#    - Identified all CSV files available in the Raw data folder.
#
# 2. Dataset Loading
#    - Loaded all CSV datasets into Pandas DataFrames.
#
# 3. Table-Level Profiling
#    - Captured the number of rows and columns for each dataset.
#
# 4. Column-Level Profiling
#    - Captured column names, data types, missing-value counts,
#      and number of unique values.
#
# 5. Missing-Value Profiling
#    - Calculated missing-value counts and percentages for
#      each column.
#
# 6. Duplicate Profiling
#    - Identified duplicate rows in each dataset.
#
# 7. Key/ID Profiling
#    - Evaluated ID columns for uniqueness and repeated values
#      to understand potential primary and foreign-key relationships.
#
# 8. Date/Time Profiling
#    - Identified date and timestamp columns and reviewed their
#      current data types.
#
# 9. Numeric Profiling
#    - Calculated minimum, maximum, mean, median, and standard
#      deviation for numeric columns.
#
# Key observations:
#    - The geolocation dataset contains a significant number
#      of duplicate records.
#    - Review comment fields contain a high percentage of
#      missing values.
#    - Several order delivery/date fields contain missing values.
#    - Some product attributes contain missing values.
#    - Date/time fields are currently stored as string data types.
#    - ID columns have different uniqueness patterns depending
#      on their role in the data model.
#
# Profiling outputs are saved in the Processed data folder:
#    - table_summary.csv
#    - column_summary.csv
#    - missing_summary.csv
#    - duplicate_summary.csv
#    - key_summary.csv
#    - date_summary.csv
#    - numeric_summary.csv
#
# Data Profiling Status: COMPLETED
# Next Phase: Data Quality Assessment
# ============================================================