from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, FunctionTransformer
from sklearn.impute import SimpleImputer
import numpy as np

NUM_FEATURES = [
    "longitude","latitude","housing_median_age",
    "total_rooms","total_bedrooms","population",
    "households","median_income"
]

CAT_FEATURES = ["ocean_proximity"]

# Only apply log to safe skewed features
SKEWED_FEATURES = [
    "total_rooms",
    "total_bedrooms",
    "population",
    "households"
]

def safe_log(X):
    return np.log1p(np.maximum(X, 0))   # 👈 prevents negative issues

def build_preprocessor():

    # Pipeline for skewed features
    skewed_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("log", FunctionTransformer(safe_log)),
        ("scaler", StandardScaler())
    ])

    # Pipeline for normal numeric features
    normal_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ])

    # ColumnTransformer split
    preprocessor = ColumnTransformer([
        ("skewed", skewed_pipeline, SKEWED_FEATURES),
        ("normal", normal_pipeline,
         list(set(NUM_FEATURES) - set(SKEWED_FEATURES))),
        ("cat",
         Pipeline([
             ("imputer", SimpleImputer(strategy="most_frequent")),
             ("onehot", OneHotEncoder(handle_unknown="ignore"))
         ]),
         CAT_FEATURES)
    ])

    return preprocessor