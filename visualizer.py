import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set professional style for charts
sns.set_theme(style="whitegrid")

def load_cleaned_data(path):
    df = pd.read_csv(path)
    df['Date'] = pd.to_datetime(df['Date'])
    return df

df = load_cleaned_data('cleaned_expenses.csv')
