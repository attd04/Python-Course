# NOT WORKING !!!!!
# if used with smptlib then would.

import requests
from twilio.rest import Client

API_KEY = "69f04e4613056b159c2761a9d9e664d2"
TWILIO_PHONE = "+13342393968"
TWILIO_ACCNT = "AC33e7abe8dc6e3c600e418ed5c3dfbf52"
TWILIO_TOKEN = "b60793426041023207aa7d2993df712c"

MY_LAT = 48.793880
MY_LONG = -97.622307

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()

weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hours in weather_slice:
    condition_code = (hours["weather"][0]["id"])
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid=TWILIO_ACCNT)
    message = client.messages \
        .create(
         body="It's going to rain today. Don't forget your ☔️.",
         from_=TWILIO_PHONE,
         to="+37069859564")

print(message.status)
