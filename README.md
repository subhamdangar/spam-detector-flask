# 📧 Spam Email Detector (Flask + Machine Learning)

This is a **Spam Email Detection web application** built using  
**Machine Learning (Naive Bayes)** and **Flask**.

Users can enter a message or email text, and the app predicts whether it is **SPAM** or **HAM**, along with a confidence score.

---

## 🚀 Features

- Machine Learning–based spam detection
- TF-IDF text vectorization
- Bernoulli Naive Bayes classifier
- Flask web application
- Confidence score for predictions
- Clean and simple UI

---

## 🧠 Machine Learning Model

- **Algorithm:** Bernoulli Naive Bayes  
- **Vectorizer:** TF-IDF  
- **Preprocessing:**  
  - Lowercasing  
  - Tokenization  
  - Stopword removal  
  - Stemming  

The trained model and vectorizer are saved using `pickle` and reused during deployment.

---

## 🖥️ Tech Stack

- Python
- Flask
- scikit-learn
- NLTK
- HTML & CSS

---

## 📂 Project Structure

Spam_Detector_App/
│
├── app.py
├── model.pkl
├── vectorizer.pkl
├── requirements.txt
│
└── templates/
└── index.html



