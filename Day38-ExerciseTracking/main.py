import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

APP_ID = os.getenv('APP_ID')
API_KEY = os.getenv('APP_KEY')
USER_NAME = os.getenv('USER_NAME')

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

inp = input('What exercise you done today : ')
parameters = {
    "query": inp,
    "gender": 'male',
    "weight_kg": 75,
    "height_cm": 185,
    "age": 18
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

sheet_endpoint = f'https://api.sheety.co/{USER_NAME}/nitheeshWorkouts/sheet1'
for exercise in result["exercises"]:
    sheet_inputs = {
        "sheet1": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    
    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)
    print(sheet_response.text)  
