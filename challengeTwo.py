import requests
import statistics

endpoint = 'https://bfhldevapigw.healthrx.co.in/campus-hiring/submit?id=RollNo'
params = {'id': 19070122039}
headers = {'Content-Type': 'application/json'}

Y = [178, 630, 277, 137, 535, 272, 165, 873, 698, 191, 490, 848, 186, 352]
secret = '901UB5'

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
