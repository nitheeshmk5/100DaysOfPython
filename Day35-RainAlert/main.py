import os
import requests
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

api_key = os.getenv('API_KEY')
lat = os.getenv('LATITUDE')
lng = os.getenv('LONGITUDE')


base_url = 'https://api.openweathermap.org/data/2.5/forecast'

params = {
    'lat': lat,
    'lon': lng,
    'cnt':4,
    'appid': api_key
}


response = requests.get(base_url, params=params)
response.raise_for_status()  

data = response.json()

will_rain = False
weather_msg = ''
for hour_data in data['list']:
    weather_code = hour_data['weather'][0]['id']

    if weather_code < 600:
        will_rain = True
        weather_msg =  hour_data['weather'][0]['description']

#Twilio
if will_rain:
    account_sid = os.getenv('ACC_SID')
    auth_token = os.getenv('AUTH_TOKEN')
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    from_=os.getenv('NUM'),
    body=f"Today's climate will be {weather_msg}.Day 35 python code exicuted with Python anywhere",
    to=os.getenv('MY_NUMBER')
    )
