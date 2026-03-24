import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("SampleSuperstore.csv")

# Show first rows
print(df.head())

# Total Sales
print("Total Sales:", df['Sales'].sum())

# Sales by Region
region_sales = df.groupby('Region')['Sales'].sum()
region_sales.plot(kind='bar', title='Sales by Region')
plt.show()
