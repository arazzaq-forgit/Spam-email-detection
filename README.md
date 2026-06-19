# 📧 Spam Email Detection using Machine Learning

## 📌 Project Overview

This project uses Machine Learning and Natural Language Processing (NLP) to classify emails as Spam or Not Spam.

The application is built using Python, Scikit-learn, and Streamlit.

---
DEMO

<img width="1920" height="923" alt="appscreenshot(2)" src="https://github.com/user-attachments/assets/d2e2b9fc-6090-4411-b3a4-3b476c35621e" />
<img width="1920" height="925" alt="appscreenshot(1)" src="https://github.com/user-attachments/assets/103f017e-444b-4279-a98e-672c78297ade" />

## 🚀 Features

- Detect Spam Emails
- Detect Legitimate Emails
- Text Preprocessing
- TF-IDF Vectorization
- Logistic Regression Model
- Interactive Streamlit Web App

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- NLTK
- Streamlit
- Joblib

---

## 📊 Model Performance

| Model | Accuracy |
|--------|----------|
| Naive Bayes | 97.98% |
| Logistic Regression | **98.33%** |

Best Model: **Logistic Regression**

---
## 🚀 Quick Prediction

```python
from predict import predict_spam

result = predict_spam("Win a free iPhone now!")
print(result)  # Output: Spam
```

No need to retrain — model is ready to use!

## 📂 Project Structure

```
spam-email-detection/
│
├── data/
├── notebooks/
├── images/
├── app.py
├── spam_model.pkl
├── vectorizer.pkl
├── requirements.txt
└── README.md
```

---

## ▶️ Run the Project

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit app

```bash
streamlit run app.py
```

## 👨‍💻 Author

Mohd Abdul Razzaq
