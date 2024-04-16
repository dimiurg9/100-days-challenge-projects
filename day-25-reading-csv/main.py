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
print(data_dic)

data_list = data["temp"].to_list()





