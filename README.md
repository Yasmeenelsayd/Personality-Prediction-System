# 🧠 Personality Prediction System (MBTI)

This repository contains a complete **Personality Prediction System** based on the **16 Personality Factors (MBTI)** questionnaire. The project covers the full machine learning pipeline: **data analysis, model selection, hyperparameter tuning, evaluation, and deployment-ready artifacts**.

The system predicts a user’s personality type using their responses to **60 psychometric questions**, encoded on a Likert scale ranging from **-3 to +3**.

---

## 📌 Project Overview

* **Problem**: Predict MBTI personality type from questionnaire responses
* **Approach**: Classical Machine Learning (KNN, SVM, Logistic Regression, Random Forest)
* **Best Model**: Tuned **K-Nearest Neighbors (KNN)**
* **Deployment**: Serialized model and label encoder for inference

---

## 📊 Dataset Description

The dataset contains responses to **60 personality questions**, numerically encoded as:

| Response           | Value |
| ------------------ | ----- |
| Fully Agree        | 3     |
| Partially Agree    | 2     |
| Slightly Agree     | 1     |
| Neutral            | 0     |
| Slightly Disagree  | -1    |
| Partially Disagree | -2    |
| Fully Disagree     | -3    |

* Target column: **Personality** (16 MBTI classes)
* Dataset source: MBTI 16 Personality Test dataset (publicly available)

---

## 🧪 Exploratory Data Analysis (EDA)

The following analyses are performed:

* Dataset inspection (shape, types, missing values)
* Distribution analysis of questionnaire responses
* Boxplots for questions (1–60)
* Personality class distribution visualization
* Duplicate and missing value checks

Visualizations include:

* Boxplots per question range
* Class count bar plots

---

## ⚙️ Machine Learning Pipeline

### 1️⃣ Preprocessing

* Dropped non-informative columns
* Renamed question columns (Q1–Q60)
* Encoded personality labels using **LabelEncoder**
* Train-test split (80% / 20%)

### 2️⃣ Model Selection

The following models were evaluated using **5-fold cross-validation**:

* Logistic Regression
* K-Nearest Neighbors (KNN)
* Support Vector Machine (SVM)
* Random Forest

### 3️⃣ Hyperparameter Tuning

KNN was fine-tuned using **GridSearchCV** with the following search space:

```python
n_neighbors: 3 → 21 (odd values)
weights: ['uniform', 'distance']
metric: ['euclidean', 'manhattan']
```

### 4️⃣ Evaluation Metrics

* Accuracy
* Confusion Matrix
* Precision, Recall, F1-score (per class)

---

## 🏆 Final Model

* **Model**: K-Nearest Neighbors (KNN)
* **Selection Method**: GridSearchCV
* **Performance**: Best cross-validation and test accuracy among evaluated models

The trained model and encoder are saved for deployment:

```text
knn_model.pkl
label_encoder.pkl
```

---

## 🚀 Deployment

This project includes a **fully interactive Streamlit web application** that allows users to complete the 60-question MBTI assessment and receive an **instant personality prediction** with a detailed explanation of each personality dimension.

### 🔧 Deployment Features

* Step-by-step questionnaire (6 questions per page)
* Progress tracking bar
* Likert-scale responses (-3 to +3)
* Real-time state management using `st.session_state`
* Personality prediction using the trained **KNN model**
* Detailed MBTI breakdown (E/I, S/N, T/F, J/P)
* Visual explanation of dominant traits
* Reset and retake assessment option

---

### ▶️ Run the Streamlit App Locally

1. Make sure the trained model files are present:

   ```text
   knn_model.pkl
   label_encoder.pkl
   ```

2. Run the Streamlit application:

   ```bash
   streamlit run app.py
   ```

3. Open the browser at:

   ```text
   http://localhost:8501
   ```

---

### 🧠 Prediction Flow

1. User answers all 60 questions
2. Responses are encoded numerically
3. Input is reshaped to match model requirements
4. KNN model predicts encoded personality class
5. LabelEncoder decodes the MBTI personality type
6. Personality explanation and traits are displayed

---

## 📁 Repository Structure

```text
├── data/
│   └── 16P.csv
├── notebooks/
│   └── Personality_Prediction.ipynb
├── deployment/
│   ├── knn_model.pkl
│   └── label_encoder.pkl
├── app.py              # (optional) Streamlit / API deployment
├── requirements.txt
└── README.md
```

---

## 📦 Requirements

* Python 3.8+
* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn
* Joblib

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔮 Future Improvements

* Add deep learning models for comparison
* Deploy live personality prediction web app
* Add explainability (feature importance / SHAP)

---

## 📜 License

This project is licensed under the **MIT License**. You are free to use, modify, and distribute it for academic or personal use.

---

## 👤 Author

Developed for educational and research purposes in **Machine Learning & Data Science**.




## 📁 Repository Structure

```text
├── data/
│   └── 16P.csv
├── notebooks/
│   └── Personality_Prediction.ipynb
├── deployment/
│   ├── knn_model.pkl
│   └── label_encoder.pkl
├── app.py              # (optional) Streamlit / API deployment
├── requirements.txt
└── README.md
```

---

## 📦 Requirements

* Python 3.8+
* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn
* Joblib

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔮 Future Improvements

* Add deep learning models for comparison
* Handle class imbalance using resampling techniques
* Deploy live personality prediction web app
* Add explainability (feature importance / SHAP)

---

## 📜 License

This project is licensed under the **MIT License**. You are free to use, modify, and distribute it for academic or personal use.

---

## 👤 Author

Developed for educational and research purposes in **Machine Learning & Data Science**.

