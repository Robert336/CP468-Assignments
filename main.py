# Authors: Robert, Ronny

from functions import *;
import csv


# Main (driver code)


# read data from csv file
with open('city_data_50.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

