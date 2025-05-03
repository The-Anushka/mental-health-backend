import requests

url = "http://127.0.0.1:5000/analyze"
data = {
    "text": "I feel completely hopeless and alone."
}

response = requests.post(url, json=data)
print(response.json())
