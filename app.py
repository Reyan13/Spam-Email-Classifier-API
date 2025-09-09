from flask import Flask, request, jsonify
import joblib

# LOADING TRAINED MODEL
model = joblib.load("spam_model.pkl")

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Spam Classifier API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    email_text = data.get("text", "")

    if not email_text:
        return jsonify({"error": "No text provided"}), 400

    prediction = int(model.predict([email_text])[0])
    prediction_label = "spam" if prediction == 1 else "ham"

    return jsonify({"prediction": prediction_label})

if __name__ == "__main__":
    app.run(debug=True)