import requests
import json

token = "2973-UtWlIhYQYGCawx"
url = "https://api.betsapi.com/v1/bet365/start_sp?token=" +token+"&FI=60504279"
result = requests.get(url)
jsonObj = json.loads(result.content)
print(jsonObj)
