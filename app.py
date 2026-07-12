from flask import Flask, request
import joblib
from security import decrypt_model
import os

app = Flask(__name__)

# Decrypt model if needed
if not os.path.exists("model.pkl"):
    decrypt_model()

model = joblib.load("model.pkl")

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        url_length = int(request.form["url_length"])
        has_ip = int(request.form["has_ip"])
        https = int(request.form["https"])
        domain_age = int(request.form["domain_age"])

        prediction = model.predict([[url_length, has_ip, https, domain_age]])

        if prediction[0] == 1:
            result = "⚠️ Phishing Website"
        else:
            result = "✅ Safe Website"

    return f"""
    <html>
    <head>
        <title>Secure ML Model</title>
    </head>

    <body style="font-family:Arial;text-align:center;margin-top:50px;">
        <h1>Secure ML Model</h1>

        <form method="POST">

        URL Length<br>
        <input name="url_length"><br><br>

        Has IP (0 or 1)<br>
        <input name="has_ip"><br><br>

        HTTPS (0 or 1)<br>
        <input name="https"><br><br>

        Domain Age<br>
        <input name="domain_age"><br><br>

        <input type="submit" value="Predict">

        </form>

        <h2>{result}</h2>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)