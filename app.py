from flask import Flask, render_template, request, redirect, url_for, session

import os
import pickle
import nltk

# nltk.download('punkt')
# nltk.download('stopwords')

import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

nltk.data.path.append(os.path.join(os.getcwd(), "nltk_data"))


app = Flask(__name__)
app.secret_key = "spam-detector-secret"

# load saved model and vectorizer
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

with open('vectorizer.pkl', 'rb') as file:
    vectorizer = pickle.load(file)

ps = PorterStemmer()

def transform_text(text):
    text = text.lower()
    words = nltk.word_tokenize(text)

    filtered = []
    for word in words:
        if word.isalnum():
            filtered.append(word)

    filtered = [
        ps.stem(word)
        for word in filtered
        if word not in stopwords.words('english')
        and word not in string.punctuation
    ]

    return " ".join(filtered)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        message = request.form["message"]

        if not message.strip():
            session.pop("result_type", None)
            session.pop("confidence", None)
            return redirect(url_for("home"))

        processed = transform_text(message)
        vector = vectorizer.transform([processed])

        prediction = model.predict(vector)[0]
        proba = model.predict_proba(vector)[0]

        if prediction == 1:
            session["result_type"] = "spam"
            session["confidence"] = f"{proba[1] * 100:.2f}"
        else:
            session["result_type"] = "ham"
            session["confidence"] = f"{proba[0] * 100:.2f}"

        return redirect(url_for("home"))


    # GET request
    result_type = session.pop("result_type", None)
    confidence = session.pop("confidence", None)
    return render_template("index.html", result_type=result_type, confidence=confidence)




if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

