import pandas as pd
import os
from .config import DATA_PATH, REMOTE_URL

def load_data():

    # If file exists, check if it's valid
    if os.path.exists(DATA_PATH):
        try:
            df = pd.read_csv(DATA_PATH)

            # Check if empty
            if df.shape[1] == 0:
                raise ValueError("Empty dataset")

            print("Loaded dataset from local disk")
            return df

        except Exception:
            print("Corrupted/empty file detected. Re-downloading...")

    # Download dataset
    print("Downloading dataset from remote source...")
    df = pd.read_csv(REMOTE_URL)

    os.makedirs("data", exist_ok=True)
    df.to_csv(DATA_PATH, index=False)

    print("Dataset downloaded and saved.")

    return df