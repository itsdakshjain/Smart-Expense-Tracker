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

def get_category_totals(dataframe):
    return dataframe.groupby('Category')['Amount'].sum().sort_values(ascending=False)

category_data = get_category_totals(df)
