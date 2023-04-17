import requests

endpoint = "http://127.0.0.1:8080/api/products/1/update/"

data = {
    "title" : "hello darkness my old friend",
    "price": 2145
}

response = requests.put(endpoint, json=data)
print(response.json())