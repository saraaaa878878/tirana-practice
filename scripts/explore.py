import pandas as pd

# Load the CSV from disk into a DataFrame in memory
df = pd.read_csv("data/apartments.csv")

# First 5 rows — a quick visual check of the data
print("=== HEAD ===")
print(df.head())

# Column names, data types, non-null counts, memory usage
print("\n=== INFO ===")
print(df.info())

# Summary statistics for numeric columns: mean, min, max, quartiles
print("\n=== DESCRIBE ===")
print(df.describe())