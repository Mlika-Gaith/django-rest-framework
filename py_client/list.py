import requests 
from getpass import getpass

username = input("What is your username?\n")
password = getpass("What is your password\n")
endpoint = "http://localhost:8080/api/auth/"
response = requests.post(endpoint, json={"username":username,"password":password})

if response.status_code == 200:
    token = response.json()['token']
    headers={
        "Authorization": f"Bearer {token}"
    }
    endpoint = "http://localhost:8080/api/products/"
    response =  requests.get(endpoint,headers=headers)
    print(response.json())
else:
    print(response.json())

#endpoint = "http://localhost:8080/api/products/"
#response = requests.get(endpoint)


#print(response.json())