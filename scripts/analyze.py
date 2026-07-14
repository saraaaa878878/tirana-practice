import pandas as pd

# Load the data
df = pd.read_csv("data/apartments.csv")

# Calculated column: price per square meter (the real measure of value)
df["price_per_sqm"] = df["price"] / df["sqm"]

# Core statistics
total_listings = len(df)
avg_price = df["price"].mean()
avg_sqm = df["sqm"].mean()

# Best deal = the row with the lowest price per sqm
best = df.loc[df["price_per_sqm"].idxmin()]

# Build the report text
report = f"""TIRANA APARTMENT MARKET - SUMMARY REPORT
=========================================

Total listings analyzed: {total_listings}
Average price:           {avg_price:,.0f} EUR
Average size:            {avg_sqm:.1f} sqm

BEST VALUE LISTING
------------------
Neighborhood:   {best['neighborhood']}
Price:          {best['price']:,.0f} EUR
Size:           {best['sqm']:.0f} sqm
Bedrooms:       {best['bedrooms']}
Price per sqm:  {best['price_per_sqm']:,.0f} EUR/sqm
"""

# Write the report to a file
with open("output/summary.txt", "w") as f:
    f.write(report)

print("Report saved to output/summary.txt")
print(report)