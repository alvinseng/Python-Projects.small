import datetime
import requests
from datetime import datetime



USERNAME = "avin"
TOKEN = "yetiyerbashadow"
GRAPH_ID = "graph1"

today = datetime.now()
DATE = today.strftime('%Y%m%d')

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Chart",
    "unit": "hours",
    "type": "int",
    "color": "kuro",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint,json=graph_config, headers=headers)
# https://pixe.la/v1/users/avin/graphs/graph1.html
# print(response.text)

pix_endpoint = f'{graph_endpoint}/{GRAPH_ID}'


pixel_config = {
    "date": DATE,
    "quantity": input("How many hours? "),
}

# response = requests.post(url=pix_endpoint,json=pixel_config, headers=headers)
# print(response.text)


# update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{DATE}"
#
# new_pixel_data = {
#     "quantity": "10"
# }
#
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{DATE}"
response = requests.delete(url=delete_endpoint,headers=headers)
print(response.text)