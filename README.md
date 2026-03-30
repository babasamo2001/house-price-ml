🏠 California House Price Prediction ML App

A production-ready Machine Learning regression web application that predicts California house prices from structured housing features.

This project demonstrates the complete ML lifecycle:

Reproducible data loading (local + remote)
Preprocessing pipeline
Feature engineering
Model benchmarking
Model persistence
Flask API deployment
Interactive browser UI
Automated testing

Screenshots
UI screenshot is stored in the assets/folder:
assets/ui.png

🖼️ App Preview

Example prediction: $471,171.00 see assets/ui.png

🚀 Project Highlights
    Dataset
California Housing Dataset
20,640 rows, ~1.37 MB
Numerical + categorical features
Target: median_house_value

Dataset is not included in the repository. (ignored in .gitignore) — only the trained model is needed for predictions.
It is automatically downloaded from a remote source if not found locally
Download the dataset here if you want to retrain: [California Housing Dataset](https://raw.githubusercontent.com/ageron/handson-ml/master/datasets/housing/housing.csv)

Ideal for fast training, quick experimentation

🧠 ML Pipeline

Built using scikit-learn Pipeline + ColumnTransformer

✔ Preprocessing
Missing value imputation
Train/test split
Numerical scaling
Categorical encoding
Local or remote reproducible loading

✔ Feature Engineering
Safe skewness correction using log transform (applied only to positive-skew features):
total_rooms, total_bedrooms, population, households
StandardScaler for normalization
OneHotEncoder for ocean_proximity
median_income represented in ×10,000 USD units, clearly shown in UI input label

🤖 Models Compared
Linear Regression
Random Forest Regressor
XGBoost Regressor

Best model selected automatically using RMSE.

📊 Current Performance
Model	RMSE
Linear Regression	~69,000
Random Forest	~48,000
XGBoost	~47,000 ✅ best

💾 Model Persistence

The full preprocessing + model pipeline is saved as:
models/pipeline.pkl
Inference is fast due to the lightweight dataset and pipeline, making cloud deployment efficient.

🌐 Web Application
Flask backend
HTML/CSS frontend
JavaScript async fetch for real-time predictions
Clear/reset buttons
Comma-formatted USD output

Example Output:

Predicted Price: $425,002.53

🧪 Testing
Pytest validates model artifact existence:
pytest

⚙️ Installation & Usage
Install dependencies:
pip install -r requirements.txt
Train the model:
python -m src.model_train
Run the web app:
python app.py
Open in browser:
http://127.0.0.1:5000

📁 Tech Stack
Python, Pandas, NumPy
scikit-learn, XGBoost
Flask
HTML, CSS, JavaScript
Pytest

🎯 Key Engineering Skills Demonstrated
Modular ML architecture
Preprocessing pipelines
Feature engineering for skewed data
Multi-model benchmarking
Backend API serving
Frontend/backend integration
Debugging and production fixes
Deployment-ready packaging

👨‍💻 Author: Adeleye Babatunde  
Portfolio-ready ML engineering project demonstrating end-to-end workflow, ideal for GitHub showcase and cloud deployment.