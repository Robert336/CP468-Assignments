# Authors: Robert, Ronny
from city import City;
from functions import DFS, BFS, AStar, distance;
import csv

# Travaling Salesman Problem
# Main (driver code)

# array containing all city objects
cities = []

# read data from csv file
with open('city_data_50.csv', 'r') as file:
    reader = csv.reader(file) 
    # skip first line
    next(reader)
    # interate through each row in the csv file
    for row in reader:
        #print(row)
        # add city object to array
        cities.append(City(row[0], row[1], float(row[2]), float(row[3])))


# arbitrary starting city to be used for all algorithms
START_CITY = cities[0]

print("DFS Solution:")
visited = []
visited, distance_traveled = DFS(START_CITY, cities, visited, 0)

print("Visited: ", visited)
print("Distance traveled: ", distance_traveled, "KM")

# reset visited and distance_traveled
visited = []
distance_traveled = 0
print("**********************************************************\n")

print("BFS Solution:")


# add BFS solution here


# reset visited and distance_traveled
visited = []
distance_traveled = 0
print("**********************************************************\n")
print("AStar Solution:")

visited, distSoFar = AStar(START_CITY, cities)
print("Visited: ", visited)
print("Distance traveled: ", distSoFar[-1], "KM")

# reset visited and distance_traveled
visited = []
print("**********************************************************\n")



