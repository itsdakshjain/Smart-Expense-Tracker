import pandas as pd
import random
from datetime import datetime, timedelta

def generate_expenses(n=100):
    categories = ['Food', 'Rent', 'Transport', 'Shopping', 'Bills']
    data = []
    for i in range(n):
        date = datetime(2025, 1, 1) + timedelta(days=random.randint(0, 180))
        data.append({
            'Date': date.strftime('%Y-%m-%d'),
            'Category': random.choice(categories),
            'Amount': round(random.uniform(5, 500), 2)
        })
    return pd.DataFrame(data)

if __name__ == '__main__':
    df = generate_expenses()
    df.to_csv('raw_expenses.csv', index=False)
    print('Raw data generated!')

    # Injecting errors for cleaning practice
    # df.loc[0:5, 'Amount'] = None
