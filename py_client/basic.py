import requests

endpoint = "http://localhost:8000/api/"

get_response = requests.get(
    endpoint, params={"abc": 123}, json={"query": "Hello world"}
)  # API -> Method
# print(get_response.text)
# print(get_response.status_code)
print(get_response.json())
