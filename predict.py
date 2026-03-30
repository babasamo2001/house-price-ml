# src/predict.py

import joblib
import pandas as pd
from src.config import PIPELINE_PATH

# Load once
pipeline = joblib.load(PIPELINE_PATH)

def make_prediction(data: dict):

    df = pd.DataFrame([data])   # preserves column names

    prediction = pipeline.predict(df)[0]

    return round(float(prediction), 2)