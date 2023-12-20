import requests
from datetime import datetime
import smtplib

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude
my_email = ""
password = ""

def check_for_minus(value):
    if value < 0:
        return -value
    else:
        return value

def is_above():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    print(iss_latitude, iss_longitude)

    iss_lat = check_for_minus(iss_latitude)
    iss_long = check_for_minus(iss_longitude)
    my_lat = check_for_minus(MY_LAT)
    my_long = check_for_minus(MY_LONG)
    lat_differnce = iss_lat - my_lat
    long_differnece = iss_long - my_long
    print(lat_differnce,long_differnece)
    if (lat_differnce < 5 and lat_differnce > -5) and (long_differnece < 5 and long_differnece > -5):
        print("ISS is above.")
        return True



is_it = is_above()
#Your position is within +5 or -5 degrees of the ISS position.

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
hour = time_now.hour
print(hour)
#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

if is_it == True and hour > sunset and hour < sunrise:
    print("asd")
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,to_addrs=my_email, msg=f"Subject: ISS is above!\n\n")

