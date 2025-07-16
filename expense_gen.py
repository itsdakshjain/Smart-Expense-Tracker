import logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
import pandas as pd
import random
from datetime import datetime, timedelta

class ExpenseGenerator:
    def __init__(self):
        self.categories = ['Food', 'Rent', 'Transport', 'Shopping', 'Bills']

    def create_data(self, n=200):
        data = []
        for i in range(n):
            date = datetime(2025, 1, 1) + timedelta(days=random.randint(0, 150))
            data.append({'Date': date.strftime('%Y-%m-%d'), 'Category': random.choice(self.categories), 'Amount': round(random.uniform(10, 800), 2)})
        return pd.DataFrame(data)

    def inject_errors(self, df):
        for _ in range(15):
            idx = random.randint(0, len(df)-1)
            df.loc[idx, 'Amount'] = None
        return df

    def get_stats(self, df):
        return df.groupby('Category')['Amount'].count()

if __name__ == '__main__':
    gen = ExpenseGenerator()
    df = gen.create_data()
    df = gen.inject_errors(df)
    df.to_csv('raw_expenses.csv', index=False)
    print('New Class-based data generated!')
