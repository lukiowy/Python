import requests
import smtplib

MY_LAT = 36.31
MY_LONG = 29.14
my_email = ""
password = ""
api_key = ""
URL = "https://api.openweathermap.org/data/2.5/forecast"
parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(url=URL, params=parameters)
response.raise_for_status()
data = response.json()

will_rain = False
for i in range(0,4):
    id = data["list"][i]["weather"][0]["id"]
    print(id)
    if int(id) < 700:
        will_rain = True
if will_rain:
    print("Bring an umbrella.")
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,to_addrs=my_email, msg=f"Subject: Bring an umbrella!!\n\n")

