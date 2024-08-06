# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 20:00:54 2024

@author: Amirkhan
"""

import pandas as pd
import numpy as np

# Мәліметтерді генерациялау
np.random.seed(42)
n_customers = 500
ages = np.random.randint(18, 70, size=n_customers)
incomes = np.random.randint(20000, 150000, size=n_customers)
spendings = np.random.randint(1000, 20000, size=n_customers)

data = {
    'CustomerID': range(1, n_customers + 1),
    'Age': ages,
    'Annual_Income': incomes,
    'Spending_Score': spendings
}

df = pd.DataFrame(data)
df.to_csv('customer_data.csv', index=False)
print("Customer data created and saved to 'customer_data.csv'")
