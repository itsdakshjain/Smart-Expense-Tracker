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
