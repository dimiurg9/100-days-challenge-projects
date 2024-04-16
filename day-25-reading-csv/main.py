'''
code required lot of cleaning. Use csv library instead
with open("weather_data.csv", 'r') as data_file:
    content = data_file.readlines()
    print(type(content[1]))
'''

"""
lot of moves to work with csv library. Use pandas
import csv

with open("weather_data.csv", 'r') as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)
"""

import pandas

data = pandas.read_csv("weather_data.csv")
data_dic = data.to_dict()
# print(data_dic)

# data_list = data["temp"].to_list()
data_list = data["temp"].to_list()
# print(data_list)
average = sum(data_list)/len(data_list)
print(f"{average:.2f}")
print("max value: " + str(max(data_list)))

# to print columns only
# columns = data.columns
print(type(data.columns))

# to print row where the temp was at the max
print(data[data.temp == max(data_list)])







