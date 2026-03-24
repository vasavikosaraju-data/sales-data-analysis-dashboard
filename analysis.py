import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("SampleSuperstore.csv")

# Convert date
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Month'] = df['Order Date'].dt.month

# Total Sales
print("Total Sales:", df['Sales'].sum())

# Sales by Region
region_sales = df.groupby('Region')['Sales'].sum()
region_sales.plot(kind='bar', title='Sales by Region')
plt.xlabel("Region")
plt.ylabel("Sales")
plt.show()

# Monthly Sales Trend
monthly_sales = df.groupby('Month')['Sales'].sum()
monthly_sales.plot(kind='line', marker='o', title='Monthly Sales Trend')
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

# Top 5 Products
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(5)
print("\nTop 5 Products:\n", top_products)

# Profit Margin
df['Profit Margin'] = df['Profit'] / df['Sales']

# Best Region by Profit
best_region = df.groupby('Region')['Profit'].sum().idxmax()
print("\nBest Region by Profit:", best_region)

# Worst Products
worst_products = df.groupby('Product Name')['Profit'].sum().sort_values().head(5)
print("\nWorst Products:\n", worst_products)
