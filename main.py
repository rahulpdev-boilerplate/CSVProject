# # Retrieve column from CSV file using csv module
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     print(data)
#     temps = []
#     next(data)
#     for row in data:
#         temps.append(int(row[1]))
#     print(temps)


# Retrieve column from CSV file using pandas module
import pandas

data = pandas.read_csv("weather_data.csv")
print(type(data))
print(type(data["temp"]))
print(data["temp"].to_list())
