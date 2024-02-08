# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         for temp in row:
#             if temp.isdigit():
#                 temperature.append(int(temp))
#         print(row)
#     print(temperature)


import pandas
import pandas as pd

data = pandas.read_csv("weather_data.csv")
# print(data)

temp_list = data["temp"].to_list()
# temp_mean = data["temp"].mean()
# temp_max = data["temp"].max()
# print(temp_max)

# print(data[data.temp == temp_max])

monday = data[data.day == "Monday"]
print(monday)
monday_temp = monday.temp[0]
print(monday_temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)


# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
# red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
#
# data_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
# }
#
# df = pandas.DataFrame(data_dict)
# df.to_csv("squirrel_count.csv")