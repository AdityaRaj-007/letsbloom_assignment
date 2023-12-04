import requests

BASE = "http://127.0.0.1:5555"

headers = {"Content-Type": "application/json"}

# Data to be sent in the request body
data = {
    "name": "Goosebumps",
    "author": "RL Stine",
    "quantity": 3
}
response = requests.post(BASE + "/api/books", json=data)
print(response)


response = requests.get(BASE + "/api/books")
print(response.json())


updated_data = {
    "name": "Goosebumps",
    "author": "RL Stine",
    "quantity": 2
}
response = requests.put(BASE + "/api/books/656dacc1e3e0242e7de98b8j", json=updated_data)
print(response.status_code)