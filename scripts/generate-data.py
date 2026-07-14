import pandas as pd
import random

# Fixed seed so the data is reproducible — same output every run
random.seed(42)

neighborhoods = [
    "Blloku", "Komuna e Parisit", "Don Bosko", "Kombinat",
    "Astir", "Fresku", "Lapraka", "21 Dhjetori", "Ali Demi", "Kinostudio"
]

# Base price per sqm (EUR) for each neighborhood — roughly realistic
price_per_sqm = {
    "Blloku": 2200, "Komuna e Parisit": 1800, "Don Bosko": 1300,
    "Kombinat": 900, "Astir": 1000, "Fresku": 950, "Lapraka": 1100,
    "21 Dhjetori": 1500, "Ali Demi": 1200, "Kinostudio": 1000
}

rows = []
for _ in range(40):
    neighborhood = random.choice(neighborhoods)
    bedrooms = random.randint(1, 4)
    sqm = random.randint(40, 60) + bedrooms * random.randint(15, 25)
    bathrooms = 1 if bedrooms <= 2 else random.randint(1, 2)
    floor = random.randint(1, 10)
    # Price = area * neighborhood rate, with some random variation (+/- 10%)
    price = int(sqm * price_per_sqm[neighborhood] * random.uniform(0.9, 1.1))

    rows.append({
        "price": price,
        "sqm": sqm,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "floor": floor,
        "neighborhood": neighborhood
    })

df = pd.DataFrame(rows)
df.to_csv("data/apartments.csv", index=False)

print(f"Saved {len(df)} rows to data/apartments.csv")