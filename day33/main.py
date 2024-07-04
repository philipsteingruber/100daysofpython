import time
from datetime import datetime

import requests

MY_LAT = 57.722225  # Your latitude
MY_LONG = 11.935108  # Your longitude
REQUEST_PARAMETERS = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}


def refresh_iss():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    return iss_latitude, iss_longitude


def refresh_sunrise_sunset():
    response = requests.get(
        "https://api.sunrise-sunset.org/json", params=REQUEST_PARAMETERS
    )
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    return sunrise, sunset


def iss_close(iss_latitude, iss_longitude):
    return abs(iss_latitude - MY_LAT) < 5 and abs(iss_longitude - MY_LONG) < 5


def sun_is_down(sunrise, sunset):
    current_hour = datetime.now().hour
    return current_hour > sunset or current_hour < sunrise


while True:
    current_iss_latitude, current_iss_longitude = refresh_iss()
    lastest_sunrise, latest_sunset = refresh_sunrise_sunset()
    if sun_is_down(lastest_sunrise, latest_sunset) and iss_close(
        current_iss_latitude, current_iss_longitude
    ):
        print("go")
    else:
        print("nope")
    print("Sleeping for 60 seconds")
    time.sleep(60)
