## Spam Email Classifier API

This project is a **REST API** built with **Flask** that classifies text messages as **spam** or **ham** using **Machine Learning**.

## Features
- Classifies messages as spam or not.
- Uses **Naive Bayes** classifier with **CountVectorizer**.
- Easy to test via **Postman**, **Python scripts**, or **curl**.
- Model is trained and saved using **joblib**.

## Tech Stack
- Python 3.12
- Flask
- pandas
- scikit-learn
- joblib
- requests (for testing API)

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/SpamClassifierAPI.git
2. Create and activate virtual environment:
   python -m venv venv
   venv\Scripts\activate   # Windows
   source venv/bin/activate # macOS/Linux
3. Install dependencies:
   pip install -r requirements.txt
4. Train the model:
   python model_training.py
5. Start the Flask server:
   python app.py
6. Test using testing_api.py or Postman.

## Testing the API
1. Using Python script (testing_api.py):
   import requests
   
   url = "http://127.0.0.1:5000/predict"
   data = {"text": "Congratulations! You won a free gift card."}

   response = requests.post(url, json=data)
   print(response.json())

2. Using Postman or curl:
   curl -X POST http://127.0.0.1:5000/predict \
   -H "Content-Type: application/json" \
   -d "{\"text\":\"You have won a lottery!\"}"


Notes:
1. Keep venv/ in .gitignore to avoid pushing virtual environment files.
2. Make sure spam.csv dataset is in the project folder before training.
3. Use jsonify in Flask routes; convert numpy.int64 to native int if needed.


License:
This project is licensed under the MIT License.




