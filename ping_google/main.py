import requests

def ping():
    res = requests.get("https://www.google.com/")

    return res.status_code 
