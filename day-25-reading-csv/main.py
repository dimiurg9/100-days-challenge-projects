'''
code required a lot of cleaning. Use csv library instead
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

"""import pandas

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
"""
"""
To create csv file with two columns Fur color and Count
and count all squirels of each color in 2018 central park document 
"""

import pandas as pd
file_from = "2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240416.csv"
file_to = "squirel_count.csv"
data = pd.read_csv(file_from)
grey_color = len(data[data['Primary Fur Color'] == 'Gray'])
cinnamon_color = len(data[ data['Primary Fur Color'] == 'Cinnamon'])
black_color = len(data[data['Primary Fur Color'] == 'Black'])

count_by_color = {
    'Primary Fur Color' : ['Gray', 'Cinnamon', 'Black'],
    'Count' : [grey_color, black_color, cinnamon_color]
}
data_to_csv = pd.DataFrame(count_by_color)
data_to_csv.to_csv(file_to, index=False, lineterminator=',\n')




