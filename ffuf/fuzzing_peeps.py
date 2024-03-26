import requests
import sys

res = requests.get(url=f"http://10.10.11.61/api")
print(res)
data = res.json()
print(data)