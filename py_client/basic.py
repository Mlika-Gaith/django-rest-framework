import requests


endpoint = "https://httpbin.org/"
endpoint = "http://127.0.0.1:8080/api/"

#response = requests.get(endpoint, params={"abc":123}, json={"query":"HEllo"}) # API
response = requests.post(endpoint, json={"title":"Hello WOrld"})
# print raw text response
print(response.text)
print(response.status_code)