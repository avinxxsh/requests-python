import requests
import statistics

endpoint = 'api_here'
params = {}
headers = {'Content-Type': 'application/json'}

Y = ['received data from get']
secret = 'XXXXX'

size = len(Y)
mean = round(statistics.mean(Y), 2)
median = statistics.median(Y)
mode = statistics.mode(Y)
min_val = min(Y)
max_val = max(Y)

payload = {
    "Size": size,
    "Mean": mean,
    "Median": median,
    "Mode": mode,
    "Min": min_val,
    "Max": max_val,
    "Secret": secret,
}
r = requests.post(endpoint, headers=headers, json=payload, params=params)

print(r.text)
