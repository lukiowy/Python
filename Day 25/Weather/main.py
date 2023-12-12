import csv
# with open("C:/Python/Day 25/weather_data.csv") as file:
#     contents = file.readlines()
#     print(contents)

# with open("C:/Python/Day 25/weather_data.csv") as file:
#     contents = csv.reader(file)
#     temperatures = []
#     for row in contents:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)
import pandas

data = pandas.read_csv("C:/Python/Day 25/Weather/weather_data.csv")
print(data)
print(data['temp'])
data_dict = data.to_dict()
print(data_dict)
temp_list = data["temp"].to_list()
print(temp_list)
all = 0
for temp in temp_list:
    all += temp
average = all/len(temp_list)
print(average)

print(data["temp"].mean())
print(data['temp'].max())

print(data[data.temp == data['temp'].max()])
monday = data[data.day == "Monday"]
print((monday.temp * 1.8) + 32)