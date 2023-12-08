import requests 
endpoint = "http://localhost:8080/api/products/"


data = {
    "title" : "Test",
    "price" : 1500.20
}

response = requests.post(endpoint, json=data)
print(response.json)