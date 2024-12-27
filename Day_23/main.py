# import csv
# with open ("weather_data.csv.csv") as data:
#     data = csv.reader(data)
#
#     for row in data:
#         print(row)
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv.csv")
# print(data)
# print(data["temp"])


import pandas
data = pandas.read_csv("weather_data.csv.csv")
data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(len(temp_list))
avg = sum(temp_list) / len(temp_list)
print(avg)

