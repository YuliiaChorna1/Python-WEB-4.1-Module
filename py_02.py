import requests


headers = {"User-Agent": "MY PYTHON SCRIPT"}

response = requests.get("http://httpbin.org/get", headers=headers)


print(response.status_code)
print(response.headers)
print(response.text)

