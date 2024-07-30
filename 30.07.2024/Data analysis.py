import pandas as pd
data = pd.read_csv('data.csv')
summary_statistics = data.describe()
grouped_data = data.groupby('category').mean()
print("Summary Statistics:")
print(summary_statistics)
print("\nGrouped Data:")
print(grouped_data)
