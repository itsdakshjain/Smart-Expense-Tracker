import pandas as pd
import os

def load_dataset(file_path):
    if os.path.exists(file_path):
        print(f"--- Loading Dataset: {file_path} ---")
        return pd.read_csv(file_path)
    else:
        print("Error: The raw data file was not found.")
        return None

df = load_dataset('raw_expenses.csv')

def check_missing_data(dataframe):
    print("\n[SCANNING FOR MISSING VALUES]")
    null_counts = dataframe.isnull().sum()
    print(null_counts[null_counts > 0])

if df is not None:
    check_missing_data(df)

def show_stats(dataframe):
    print("\n--- Descriptive Statistics ---")
    print(dataframe.describe())
    print("\nCategory Counts:")
    print(dataframe['Category'].value_counts())

show_stats(df)

def fix_missing_amounts(dataframe):
    print("\n[ACTION: Filling Missing Amounts]")
    avg_val = dataframe['Amount'].mean()
    dataframe['Amount'] = dataframe['Amount'].fillna(avg_val)
    print(f"Filled missing values with mean: {avg_val:.2f}")
    return dataframe

df = fix_missing_amounts(df)
