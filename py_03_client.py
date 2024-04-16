import requests

json_body = {"friends_id": "3"}
# response = requests.post("http://127.0.0.1:8001/friends", json=json_body)
response = requests.delete("http://127.0.0.1:8001/friends")

print(response.status_code)
print(response.text)
