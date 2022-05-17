import requests

endpoint = 'http://localhost:8000/employees/'

get_response = requests.get(endpoint)

print(get_response.json())