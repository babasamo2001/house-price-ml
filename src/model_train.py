import os
import joblib
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor

from .data_loader import load_data
from .preprocessing import build_preprocessor
from .config import TARGET, PIPELINE_PATH, MODEL_DIR


def train():

    df = load_data()

    X = df.drop(TARGET, axis=1)
    y = df[TARGET]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    models = {
        "LinearRegression": LinearRegression(),
        "RandomForest": RandomForestRegressor(n_estimators=200),
        "XGBoost": XGBRegressor(n_estimators=200)
    }

    best_model = None
    best_rmse = float("inf")

    for name, model in models.items():

        pipeline = Pipeline([
            ("preprocessor", build_preprocessor()),
            ("model", model)
        ])

        pipeline.fit(X_train, y_train)

        preds = pipeline.predict(X_test)

        import numpy as np

        mse = mean_squared_error(y_test, preds)
        rmse = np.sqrt(mse)

        print(f"{name} RMSE: {rmse}")

        if rmse < best_rmse:
            best_rmse = rmse
            best_model = pipeline

    os.makedirs(MODEL_DIR, exist_ok=True)
    joblib.dump(best_model, PIPELINE_PATH)

    print("Best model saved → models/pipeline.pkl")


if __name__ == "__main__":
    train()