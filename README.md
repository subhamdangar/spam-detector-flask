<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Flask-3.0-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/scikit--learn-1.6-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="scikit-learn">
  <img src="https://img.shields.io/badge/Deployed_on-Render-46E3B7?style=for-the-badge&logo=render&logoColor=white" alt="Render">
</p>

<h1 align="center">🛡️ SpamShield AI</h1>

<p align="center">
  <strong>An intelligent spam email detector powered by Machine Learning and Flask.</strong><br>
  Paste any email or SMS message and get an instant spam-or-ham prediction with a confidence score.
</p>

<p align="center">
  <a href="https://spam-detector-flask.onrender.com"><strong>🌐 Live Demo on Render →</strong></a>
</p>

---

## ✨ Features

- **Real-time Spam Detection** — Paste any message and get an instant prediction.
- **Confidence Score** — See how confident the model is with a visual progress bar.
- **NLP Preprocessing Pipeline** — Lowercasing → Tokenization → Stopword Removal → Porter Stemming.
- **Beautiful Dark UI** — Glassmorphism design with animated gradients, floating particles, and smooth micro-interactions.
- **Responsive Design** — Works seamlessly on desktop, tablet, and mobile.
- **Deployed & Live** — Running on [Render](https://render.com) for instant access.

---

## 🧠 Machine Learning Pipeline

| Stage | Detail |
|---|---|
| **Dataset** | [SMS Spam Collection](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset) — 5,574 SMS messages labeled as `spam` or `ham` |
| **Text Preprocessing** | Lowercasing, tokenization (`nltk.word_tokenize`), stopword removal, punctuation removal, Porter stemming |
| **Feature Extraction** | TF-IDF Vectorization (`TfidfVectorizer` from scikit-learn) |
| **Classifier** | Bernoulli Naive Bayes (`BernoulliNB`) |
| **Serialization** | Trained model & vectorizer saved via `pickle` (`model.pkl`, `vectorizer.pkl`) |

The full training notebook with EDA, data cleaning, and model evaluation is available at [`notebooks/spam_email_detection.ipynb`](notebooks/spam_email_detection.ipynb).

---

## 🖥️ Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | Python 3.11+, Flask 3.0 |
| **ML / NLP** | scikit-learn, NLTK, NumPy, SciPy |
| **Frontend** | HTML5, CSS3 (glassmorphism, animations), Vanilla JS |
| **Fonts** | [Inter](https://fonts.google.com/specimen/Inter) (Google Fonts) |
| **Deployment** | [Render](https://render.com) (Web Service) |

---

## 📂 Project Structure

```text
Spam_Detector_App/
├── app.py                 # Flask application & prediction logic
├── model.pkl              # Trained Bernoulli Naive Bayes model
├── vectorizer.pkl         # Fitted TF-IDF vectorizer
├── nltk_setup.py          # NLTK data downloader utility
├── requirements.txt       # Python dependencies
├── README.md              # This file
│
├── data/
│   └── spam.csv           # SMS Spam Collection dataset
│
├── notebooks/
│   └── spam_email_detection.ipynb   # Model training & EDA notebook
│
└── templates/
    └── index.html         # Frontend UI template
```

---

## ⚙️ Local Setup & Installation

### Prerequisites

- Python 3.11 or higher
- pip package manager
- Git

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/subhamdangar/spam-detector-flask.git
cd spam-detector-flask

# 2. (Recommended) Create a virtual environment
python -m venv venv
source venv/bin/activate        # macOS/Linux
# venv\Scripts\activate         # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Download NLTK data
python nltk_setup.py

# 5. Run the application
python app.py
```

The app will start on **http://localhost:5000**. Open it in your browser and start detecting spam!

---

## 🌐 Deployment (Render)

This app is deployed on [Render](https://render.com) as a Web Service.

**Live URL:** [https://spam-detector-flask.onrender.com](https://spam-detector-flask.onrender.com)

### Render Configuration

| Setting | Value |
|---|---|
| **Build Command** | `pip install -r requirements.txt && python nltk_setup.py` |
| **Start Command** | `python app.py` |
| **Environment** | Python 3 |

> **Note:** The Render free tier may spin down the service after inactivity. The first request after a cold start may take 30–60 seconds.

---

## 🔌 How It Works

```
User Input (email/SMS text)
        │
        ▼
┌──────────────────────┐
│  Text Preprocessing  │  Lowercase → Tokenize → Remove Stopwords → Stem
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│   TF-IDF Vectorizer  │  Transforms text into numerical feature vector
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│  Bernoulli Naive     │  Predicts: SPAM (1) or HAM (0)
│  Bayes Classifier    │  Returns: class probabilities
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│  Result + Confidence │  Displayed in the UI with animated progress bar
└──────────────────────┘
```

---

## 📊 Sample Predictions

| Input Message | Prediction | Confidence |
|---|---|---|
| *"Congratulations! You've won a $1000 gift card. Click here to claim."* | 🚫 SPAM | ~98% |
| *"Hey, are we still meeting for lunch tomorrow?"* | ✅ HAM | ~99% |
| *"URGENT: Your account has been compromised. Verify now!"* | 🚫 SPAM | ~96% |
| *"The meeting notes from today are attached. Let me know your thoughts."* | ✅ HAM | ~98% |

---

## 📦 Dependencies

```text
flask==3.0.0
scikit-learn==1.6.1
nltk==3.8.1
numpy
scipy
```

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 👨‍💻 Author

**Subham Dangar**

- GitHub: [@subhamdangar](https://github.com/subhamdangar)

---

<p align="center">
  <sub>Built with ❤️ using Python, Flask & Machine Learning</sub>
</p>