# Authors: Robert, Ronny
from city import City;
from functions import *;
import csv


# Main (driver code)

cities = []


# read data from csv file
with open('city_data_50.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
        cities.append(City(row[0], row[1], row[2], row[3]))


