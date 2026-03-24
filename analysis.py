# Profit Margin
df['Profit Margin'] = df['Profit'] / df['Sales']

# Best Region by Profit
best_region = df.groupby('Region')['Profit'].sum().idxmax()
print("Best Region by Profit:", best_region)

# Worst Products (Loss making)
worst_products = df.groupby('Product Name')['Profit'].sum().sort_values().head(5)
print("\nWorst Products:\n", worst_products)
