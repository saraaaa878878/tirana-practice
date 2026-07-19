"""Train a linear regression model to predict apartment prices."""

from pathlib import Path

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

# Build the path from the script's location, so it works
# no matter which folder you run the script from.
DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "apartments.csv"

FEATURES = ["sqm", "bedrooms", "bathrooms", "floor"]
TARGET = "price"


def main():
    # 1. Load the data
    df = pd.read_csv(DATA_PATH)

    # 2. Drop rows with missing values in the columns we use,
    #    because LinearRegression cannot handle NaN.
    df = df.dropna(subset=FEATURES + [TARGET])

    # 3. Separate features (X) and target (y)
    X = df[FEATURES]
    y = df[TARGET]

    # 4. Split: 80% for training, 20% for testing.
    #    random_state=42 makes the split reproducible.
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # 5. Train the model on the training set only
    model = LinearRegression()
    model.fit(X_train, y_train)

    # 6. Evaluate on the unseen test set
    y_pred = model.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)

    print(f"Rows used: {len(df)} (train: {len(X_train)}, test: {len(X_test)})")
    print(f"R2 score on test set: {r2:.3f}")
    print(f"Mean absolute error on test set: {mae:,.0f}")


if __name__ == "__main__":
    main()