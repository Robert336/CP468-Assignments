# Authors: Robert, Ronny
from city import City;
from functions import *;
import csv


# Main (driver code)

# array containing all city objects
cities = []

# read data from csv file
with open('city_data_50.csv', 'r') as file:
    reader = csv.reader(file) # skip first line
    # interate through each row in the csv file
    for row in reader:
        print(row)
        # add city object to array
        cities.append(City(row[0], row[1], row[2], row[3]))


