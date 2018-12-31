import requests

def callUpcomingEvent():
    token = "2973-UtWlIhYQYGCawx"
    url = "https://api.betsapi.com/v2/events/upcoming?sport_id=1&token={}".format(token)

    res = requests.get(url)
    return res.json()



