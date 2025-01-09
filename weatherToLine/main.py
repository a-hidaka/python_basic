import requests
import weather_api



token = "VPfMDUmR43ZC8FWAjOYMRiitzTzJBf82EZNJHCarPry"

def LINE_message(msg):
    url = "https://notify-api.line.me/api/notify"

    headers = {"Authorization":"Bearer " + token}

    message = (msg)
    
    
    payload = {"message" : message}

    r = requests.post(url,headers=headers,params=payload)

LINE_message(weather_api.message)