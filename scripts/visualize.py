import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("data/apartments.csv")

# --- Chart 1: Histogram of prices ---
plt.figure(figsize=(8, 5))
plt.hist(df["price"], bins=10, color="steelblue", edgecolor="black")
plt.title("Price Distribution of Tirana Apartments")
plt.xlabel("Price (EUR)")
plt.ylabel("Number of Apartments")
plt.tight_layout()
plt.savefig("output/price_distribution.png")
plt.close()

# --- Chart 2: Average price by bedroom count ---
avg_price = df.groupby("bedrooms")["price"].mean()

plt.figure(figsize=(8, 5))
plt.bar(avg_price.index, avg_price.values, color="darkorange", edgecolor="black")
plt.title("Average Price by Number of Bedrooms")
plt.xlabel("Bedrooms")
plt.ylabel("Average Price (EUR)")
plt.xticks(avg_price.index)
plt.tight_layout()
plt.savefig("output/avg_price_by_bedrooms.png")
plt.close()
# --- Chart 3: Scatter plot of price vs sqm ---
plt.figure(figsize=(8, 5))
plt.scatter(df["sqm"], df["price"], color="seagreen", edgecolor="black")
plt.title("Price vs Size of Tirana Apartments")
plt.xlabel("Size (sqm)")
plt.ylabel("Price (EUR)")
plt.tight_layout()
plt.savefig("output/price_vs_sqm.png")
plt.close()
print("Saved 3 charts to output/")