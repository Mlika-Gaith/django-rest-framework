import requests

product_id = input("What is the input id ?\n")
try:
    product_id = int(product_id)
except:
    print(f'{product_id} not a valid id')

if (product_id):
    # print(f"http://127.0.0.1:8080/api/products/{product_id}/delete/")
    endpoint = f"http://127.0.0.1:8080/api/products/{product_id}/delete/"
    response = requests.delete(endpoint)
    print(response.status_code==204)