# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 20:03:08 2024

@author: Amirkhan
"""

import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# Мәліметтерді оқу
df = pd.read_csv('customer_data.csv')

# KMeans моделін құру
kmeans = KMeans(n_clusters=5, random_state=42)
df['Cluster'] = kmeans.fit_predict(df[['Age', 'Annual_Income', 'Spending_Score']])

# Әр кластердің орталықтарын көрсету
print("Кластер орталықтары:")
print(kmeans.cluster_centers_)

# Кластерленген мәліметтерді визуализациялау
plt.figure(figsize=(10, 8))
sns.scatterplot(data=df, x='Annual_Income', y='Spending_Score', hue='Cluster', palette='Set1', s=100)
plt.title('Тұтынушылар кластерлері')
plt.xlabel('Жылдық кіріс')
plt.ylabel('Жұмсау көрсеткіші')
plt.legend(title='Cluster')
plt.savefig('customer_clusters.png')
plt.show()
