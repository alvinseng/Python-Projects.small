import os
import time
from data_manager import DataManager
dm = DataManager()
sheet_data = dm.get_destination_data()
from flight_search import FlightSearch
flight_search = FlightSearch()

for row in sheet_data:
    if row ["iataCode"] == "":
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        time.sleep(2)
print(f"Sheet Data: \n {sheet_data}")

dm.destination_data = sheet_data
dm.update_destination_data()


