# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 20:01:43 2024

@author: Amirkhan
"""

import pandas as pd
import matplotlib.pyplot as plt

# Мәліметтерді оқу
df = pd.read_csv('customer_data.csv')

# Негізгі статистикаларды көрсету
print("Мәліметтердің негізгі статистикасы:")
print(df.describe())

# Графиктер жасау
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.hist(df['Age'], bins=15, color='skyblue', edgecolor='black')
plt.title('Жасы бойынша үлестіру')

plt.subplot(2, 2, 2)
plt.hist(df['Annual_Income'], bins=15, color='lightgreen', edgecolor='black')
plt.title('Жылдық кірісі бойынша үлестіру')

plt.subplot(2, 2, 3)
plt.hist(df['Spending_Score'], bins=15, color='salmon', edgecolor='black')
plt.title('Жұмсау көрсеткіші бойынша үлестіру')

plt.tight_layout()
plt.savefig('customer_data_distribution.png')
plt.show()
