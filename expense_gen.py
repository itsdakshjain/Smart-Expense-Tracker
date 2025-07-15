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
