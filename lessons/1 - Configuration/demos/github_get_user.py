import requests
import json
from pprint import pprint

from google.colab import userdata

token = userdata.get('ghtoken')

response = requests.get(url='https://api.github.com/user',
                        headers={'Authorization': 'Bearer ' + token})

# print raw response
print(response.status_code)
print(response.text)

# parse json
response_json = json.loads(response.text)
pprint(response_json)

# print some values
print('Username: ' + response_json['login'])
print('Name: ' + response_json['name'])
