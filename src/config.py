from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "data/housing.csv"
REMOTE_URL = "https://raw.githubusercontent.com/ageron/handson-ml/master/datasets/housing/housing.csv"

TARGET = "median_house_value"

MODEL_DIR = BASE_DIR / "models"
PIPELINE_PATH = MODEL_DIR / "pipeline.pkl"