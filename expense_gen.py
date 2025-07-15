import pandas as pd
import random
from datetime import datetime, timedelta

class ExpenseGenerator:
    def __init__(self):
        self.categories = ['Food', 'Rent', 'Transport', 'Shopping', 'Bills']
