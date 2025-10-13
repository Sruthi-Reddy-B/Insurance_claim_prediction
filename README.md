# Insurance Claim Prediction — End-to-End ML Pipeline

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Sruthi-Reddy-B/Insurance_claim_prediction/blob/main/notebooks/eda_model_training.ipynb)

##  Project Overview
Predicts whether an insurance claim will be approved using **Random Forest**.  
This end-to-end pipeline includes: data preprocessing, model training, evaluation, and a **simple Flask web app demo**.

---

##  Tech Stack
- **Python Libraries:** Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, Joblib  
- **Web App:** Flask  
- **Environment:** Google Colab (GPU optional)

---

##  Dataset
- **Demo dataset:** `data/sample_claims.csv` (30 rows, balanced)  
- **Features:** Age, Vehicle Age, Vehicle Damage, Policy Sales Channel, Vintage, Previously Claimed  
- **Target:** Claim_Approved (0 = Not Approved, 1 = Approved)

---

##  Folder Structure
```
insurance-claim-prediction/
├── data/ # CSV dataset
│ └── sample_claims.csv
├── notebooks/ # EDA & model training
│ └── eda_model_training.ipynb
├── src/ # Saved model
│ └── claim_model.pkl
├── results/ # Evaluation plots
│ └── confusion_matrix.png
├── app/ # Flask demo
│ └── app.py
├── requirements.txt # Dependencies
└── README.md
```

---

##  How to Run

### 1️. Using Google Colab (Recommended)
1. Click the **Colab badge** at the top.  
2. Run all notebook cells sequentially.  
3. The model will train, evaluate, and generate plots in `results/`.

### 2️. Locally
```bash
# Install dependencies
pip install -r requirements.txt

# Run the notebook for training
jupyter notebook notebooks/eda_model_training.ipynb

# Run Flask demo
python app/app.py
```
Open http://127.0.0.1:5000 in your browser.

---

##  Results
Dataset: 100-row realistic demo dataset
Test set size: 43 rows (40% of total)
Accuracy: 88%
Confusion Matrix: Saved in results/confusion_matrix.png
```
| Class | Precision | Recall | F1-score | Support |
| ----- | --------- | ------ | -------- | ------- |
| 0     | 0.83      | 0.88   | 0.86     | 17      |
| 1     | 0.92      | 0.88   | 0.90     | 26      |
```

Note: Metrics are for demonstration purposes. Real-world performance depends on dataset size and quality.

---

##  Next Steps / Enhancements

- Increase dataset size for real-world use.
- Experiment with other ML models (Logistic Regression, XGBoost).
- Add interactive Colab demo for user inputs.
- Improve Flask UI for a more polished presentation.

---

## License
MIT
