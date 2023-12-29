import requests
from datetime import datetime
APP_ID = ""

API_KEY = ""
URL = ""
POST = ""
SHEETY_GET = ""
SHEETY_POST = ""
TOKEN = ""
parameters = {
    "query": input("Type your exercise: "),
    "gender": "",
    "weight_kg": ,
    "height_cm": ,
    "age": ,
}

header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

response = requests.post(url=URL, json=parameters, headers=header)
data = response.json()

name = data["exercises"][0]["name"]
duration = data["exercises"][0]["duration_min"]
cal = data["exercises"][0]["nf_calories"]

time_now = datetime.now()

sheety_params = {
    "workout": {
    "date": time_now.strftime("%d/%m/%Y"),
    "time": time_now.strftime("%H:%M:%S"),
    "exercise": name,
    "duration": duration,
    "calories": cal
    }
}

header = {
    "Authorization": f"Bearer {TOKEN}"
}

response = requests.post(url=SHEETY_POST, json=sheety_params,headers=header)
print(response.text)