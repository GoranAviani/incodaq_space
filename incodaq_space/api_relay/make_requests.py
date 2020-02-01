import requests

def make_iss_api_call(**kwargs):
    result = requests.get("http://api.open-notify.org/astros.json")
    print (result)

