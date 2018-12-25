import requests

token = "2973-UtWlIhYQYGCawx"
url = "https://api.betsapi.com/v2/events/upcoming?sport_id=1&token={}".format(token)

res = requests.get(url)

print(res.content)



