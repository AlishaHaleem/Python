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

print(data['temp'].mean())
print(data['temp'].max())

#Get data in columns
print(data['condition'])
print(data.condition)

#Get data in row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = (data[data.day == "Monday"])
print(monday.condition)



# Data frame from scratch
data_dict = {
    "students": ["Amy", "Jenny", "Raj"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")