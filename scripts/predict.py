"""Load the trained price model and predict the price of one apartment."""

from pathlib import Path

import joblib
import pandas as pd

MODEL_PATH = Path(__file__).resolve().parent.parent / "models" / "price_model.joblib"

# The made-up apartment we want a price prediction for.
APARTMENT = {
    "sqm": 75,
    "bedrooms": 2,
    "bathrooms": 1,
    "floor": 3,
}


def main():
    # 1. Load the trained model from disk (no retraining needed)
    model = joblib.load(MODEL_PATH)

    # 2. Build a one-row DataFrame with the same column names/order
    #    used during training, since the model expects that shape.
    X_new = pd.DataFrame([APARTMENT])

    # 3. Predict. predict() always returns an array (even for one row),
    #    so we take the first element with [0].
    predicted_price = model.predict(X_new)[0]

    print(f"Apartment: {APARTMENT}")
    print(f"Predicted price: {predicted_price:,.0f}")


if __name__ == "__main__":
    main()