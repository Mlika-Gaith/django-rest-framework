import requests

endpoint = "http://127.0.0.1:8080/api/products/1/"

response = requests.get(endpoint)
print(response.json())