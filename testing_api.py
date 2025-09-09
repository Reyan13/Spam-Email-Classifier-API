import requests

url = "http://127.0.0.1:5000/predict"
data = {"text": "Nah I don't think he goes to usf, he lives around here though"}

response = requests.post(url, json=data)
print(response.json())  # Should print {"prediction": "spam"} or "ham"}
