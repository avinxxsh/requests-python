import requests

get_endpoint = 'https://bfhldevapigw.healthrx.co.in/campus-hiring/input?id=RollNo'
params = {'id': 19070122039}

r = requests.get(get_endpoint, params=params)
print(r.text)

# data = r.content

# post_endpoint = 'https://bfhldevapigw.healthrx.co.in/campus-hiring/submit?id=RollNo'
# headers = {''}
