from flask import Flask, render_template, request, redirect, url_for, session


import pickle
import nltk
# nltk.download('punkt')
# nltk.download('stopwords')

import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

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
            session.pop("result", None)
            return redirect(url_for("home"))

        processed = transform_text(message)
        vector = vectorizer.transform([processed])

        prediction = model.predict(vector)[0]
        proba = model.predict_proba(vector)[0]

        if prediction == 1:
            confidence = proba[1] * 100
            session["result"] = f"SPAM 🚫 (Confidence: {confidence:.2f}%)"
        else:
            confidence = proba[0] * 100
            session["result"] = f"HAM ✅ (Confidence: {confidence:.2f}%)"

        return redirect(url_for("home"))


    # GET request
    result = session.pop("result", None)   # 🔥 clears after one display
    return render_template("index.html", result=result)




if __name__ == "__main__":
    app.run(debug=True)
