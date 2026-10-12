# opening the weather data with open function

with open('weather_data.csv') as weather_data:
    data = weather_data.readlines()
    print(data)

# better way to read csv
import csv
with open('weather_data.csv') as weather_data_2:
    data_2 = csv.reader(weather_data_2)

    temperatures = []
    for row in data_2:
            if row[1] != 'temp':
                temperatures.append(int(row[1]))
print(temperatures)

# easiest way to get it done!!!
import pandas
data_p = pandas.read_csv('weather_data.csv')
temperatures_pandas = data_p['temp'].to_list()
print(temperatures_pandas)

# CHALLENGE : you have to print condition from the weather_data
condition_pandas = data_p['condition'].to_list()
print(condition_pandas)