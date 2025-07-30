import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
from pprint import pprint

from Quizzler.data import response

load_dotenv()

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/285809dcdbfc660d8ba633e5e918fb00/flightDeals/prices"

class DataManager:

    def __init__(self):
        self._user = os.environ["SHEETY_USER"]
        self._password = os.environ["SHEETY_PASS"]
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}


    def get_destination_data(self):
        response=requests.get(url=SHEETY_PRICES_ENDPOINT, auth=self._authorization)
        data = response.json()
        self.destination_data = data["prices"]
        # pprint(data)

        return self.destination_data


    def update_destination_data(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }

            response = requests.put(
                url = f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json = new_data,
                auth= self._authorization
            )

            print(response.text)