import requests
import yaml
from pprint import pprint

with open('github_config.yml', 'r') as f:
    config = yaml.load(f)

response = requests.get(url='https://api.github.com/user',
                        headers={'Authorization': 'Bearer ' + config['token']})

# print raw response
print(response.status_code)
print(response.text)

# parse json
response_json = response.json()
pprint(response_json)

# print some values
print('Username: ' + response_json['login'])
print('Name: ' + response_json['name'])
