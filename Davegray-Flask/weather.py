from dotenv import load_dotenv
import requests
from pprint import pprint
import os

load_dotenv()

API_KEY = os.getenv('API_KEY')

def get_weather(lat = os.getenv('LAT') ,lng = os.getenv('LNG')):
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&appid={API_KEY}')

    return res.json()

if __name__ == '__main__':
    pprint(get_weather())