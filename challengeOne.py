import requests

get_endpoint = 'api_here'
params = {}

r = requests.get(get_endpoint, params=params)
print(r.text)


