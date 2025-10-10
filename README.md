# Insurance Claim Prediction — End-to-End ML Pipeline

## Overview
Predicts whether an insurance claim will be approved using Random Forest. Includes data preprocessing, model training, evaluation, and a simple Flask web app for demo.

## Tech Stack
Python, Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, Flask, Joblib

## Folder Structure
- `data/` — sample CSV data
- `notebooks/` — EDA & model training
- `src/` — saved model
- `app/` — Flask app
- `results/` — evaluation plots
- `requirements.txt` — dependencies

## How to Run
1. Install dependencies:
  pip install -r requirements.txt
2. Run the notebook for EDA and training (`notebooks/eda_model_training.ipynb`)
3. Run the Flask app for demo:
  python app/app.py

Open `http://127.0.0.1:5000` in your browser.

## Results
- Accuracy on sample data: ~100% (small dataset)
- Confusion matrix plot included in `results/`

## License
MIT
