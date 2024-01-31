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

data = pandas.read_csv("weather_data.csv")
# # print(data)
#
# temp_list = data["temp"].to_list()
# temp_mean = data["temp"].mean()
temp_max = data["temp"].max()
# print(temp_max)

# print(data[data.temp == temp_max])

monday = data[data.day == "Monday"]
monday_temp = monday.temp[0]
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)