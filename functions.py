from math import sin, cos, sqrt, atan2, radians, asin
import csv
from queue import PriorityQueue
from sys import maxsize
from itertools import permutations


# Calculate distance between two points on the Earth using Haversine formula
def distance(lat1, lon1, lat2, lon2):
    # source: https://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points

    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
    return abs(c * r)




def DFS(startCity, cities):
    # run time will be O(V + E) where V is the number of cities and E is the number of edges
    # V = 50, E = 50 * 50 = 2500

    distance_traveled = 0
    visited = []
    frontier = []
    frontier.append(startCity)

    # while stack is not empty
    while len(frontier) > 0:
        current = frontier.pop()
        if current not in visited:
            visited.append(current)

            # for each city in cities that we have been to
            for next in cities:
                if next not in visited:
                    frontier.append(next) # add city to stack
            
            # calculate distance traveled
            distance_traveled += distance(current.latitude, current.longitude, frontier[-1].latitude, frontier[-1].longitude)

    return visited, distance_traveled
    """
    output:
    DFS Solution:
    Visited:  [Alabama, Wyoming, Wisconsin, West Virginia, Washington, Virginia, Vermont, Utah, Texas, Tennessee, South Dakota, South Carolina, Rhode Island, Pennsylvania, Oregon, Oklahoma, Ohio, New York, North Dakota, North Carolina, New Mexico, New Jersey, New Hampshire, Nevada, Nebraska, Montana, Missouri, Mississippi, Minnesota, Michigan, Massachusetts, Maryland, Maine, Louisiana, Kentucky, Kansas, Iowa, Indiana, Illinois, Idaho, Georgia, Florida, Hawaii, Delaware, Connecticut, Colorado, California, Arkansas, Arizona, Alaska]
    Distance traveled:  95137.93332557622 KM
    **********************************************************
    """
    
def BFS(startCity, cities):
    # BFS here
    
    #set the cities visted to an empty list
    visited = []

    # go through all cities and append them to visited, aside from the starting city
    for i in cities:
        # checks if i is not the starting city
        if i != startCity:
            visited.append(i)


    distance_traveled = visited
    #permuations to calcluate n!, which in this case would be 50!
    next_factorial = permutations(visited)
    # run a while loop for the next permutation in the list 50! 49! 48!... 
    # once next_factorial is less than or equal to one stop the loop as there are no more factorals to be calculated
    while next_factorial <= 1:
        current = 0

        # setting variable k to the starting city 
        k = startCity

        #for loop for calculating the cost of the path
        for j in i:
            # adding the longitude and latitude of the current and next permutation 
            current_path += distance(current.latitude, current.longitude, distance_traveled.latitude, distance_traveled.longitude)
            
            #incrementing k to the current paths longitude and latitude 
            k = current.latitude & current.longitude

        # setting current path to the value of k and startCity
        current_path += k & startCity

        # setting the total distance travelled 
        distance_traveled = min(distance_traveled, current)




    return distance_traveled, visited
            
        

def AStar(startCity, cities):
    # Intial state: startCity
    # Goal state: reach all cities, and return to startCity
    # Heuristic: distance between current city and each city in cities
    # Edge cost: distance between current city and next city
    # Successor function: return all cities that are not visited
    
    # run time will be O(n!)

    frontier = PriorityQueue()
    frontier.put((0, startCity)) # .put((distance from last city, city object))

    cameFrom = [] # list of cities we have visited
    distSoFar = [] # distance traveled to each city

    #cameFrom.append(startCity)
    #distSoFar.append(0)
    
    while frontier.qsize() > 0:
        #print("frontier: ", frontier.qsize())
        current = frontier.get() # get city with lowest distance from last city

        # current is a tuple, so we need to unpack it
        current_dist = current[0]
        current = current[1]

        # if we have not visited this city yet, add it to our list of visited cities
        if current not in cameFrom:
            cameFrom.append(current)
            distSoFar.append(current_dist)
            for next in cities: # for each city in cities
                if next not in cameFrom: # if we have not visited this city yet
                    # calculate distance (cost) between current city and next city
                    newCost = distSoFar[-1] + distance(current.latitude, current.longitude, next.latitude, next.longitude)
                    # add city and it's dsitance (cost) to frontier AKA priority queue
                    frontier.put((newCost, next))
    
    # calculate the distance of traveling back to our starting city
    distSoFar[-1] += distance(cameFrom[-1].latitude, cameFrom[-1].longitude, cameFrom[0].latitude, cameFrom[0].longitude)
    cameFrom.append(cameFrom[0])
                    
    return cameFrom, distSoFar
    """
    output:
    AStar Solution:
    Visited:  [Alabama, Georgia, Florida, Mississippi, Tennessee, Louisiana, South Carolina, Arkansas, Kentucky, West Virginia, North Carolina, Indiana, Missouri, Illinois, Ohio, Virginia, Oklahoma, Texas, Kansas, Maryland, Michigan, Iowa, Pennsylvania, Wisconsin, Delaware, Nebraska, New Jersey, Minnesota, New York, Connecticut, Rhode Island, Massachusetts, New Hampshire, Vermont, South Dakota, New Mexico, Colorado, Wyoming, Maine, North Dakota, Arizona, Utah, Montana, Idaho, Nevada, California, Oregon, Washington, Alaska, Hawaii, Alabama]
    Distance traveled:  14160.096858141367 KM
    **********************************************************
    """
