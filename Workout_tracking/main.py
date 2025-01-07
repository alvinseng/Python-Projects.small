import requests
from datetime import datetime

GENDER = 'Male'
WEIGHT_KG = '91'
HEIGHT_CM = '177.8'
AGE = '30'

exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

sheet_endpoint = 'https://api.sheety.co/b44565df43ee7fa006abdf97526b62e7/workoutTracking/sheet1'

exercise_input = input("What exercise did you do?:\n")

APP_ID = "a8c73fb7"
API_KEY = "2a63fb7cb80e865b93b9230bb61f3ce5"

headers = {
    "APP_ID": APP_ID,
    "API_KEY": API_KEY,
}

parameters = {
    "query": exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

today_date = datetime.now().strftime("%m/%d/%Y")
now_time = datetime.now().strftime("%X")




