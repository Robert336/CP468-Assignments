from math import sin, cos, sqrt, atan2, radians, asin
import csv
from queue import PriorityQueue


# Calculate distance between two points on the Earth using Haversine formula
def distance(lat1, lon1, lat2, lon2):

    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
    return c * r

def DFS(startCity, cities, visited, distance_traveled):
    # DFS here
    
    if visited is None:
        visited = []
    
    visited.append(startCity) # add start city to visited

    print("in ", startCity)

    for next in cities:
        if next not in visited:
            print("Visiting ", next)

            # calculate distance between current city and next city, and add to distance_traveled
            distance_traveled += distance(startCity.latitude, startCity.longitude, next.latitude, next.longitude)
            visited.append(next) # add next city to visited

            # call DFS with next city
            DFS(next, cities, visited, distance_traveled)
    
    # if we have traveled to all cities, return to our starting city
    if len(visited) == len(cities):
        # calculate the distance of traveling back to our starting city
        print("Visited all cities, returning to ", visited[0])
        distance_traveled += distance(startCity.latitude, startCity.longitude, visited[0].latitude, visited[0].longitude)

    return visited, distance_traveled

def BFS(startCity, cities, visited, distance_traveled):
    # BFS here
    if visited is None:
        visited = []

    
        



    
    return

def AStar(startCity, cities):
    # Intial state: startCity
    # Goal state: reach all cities, and return to startCity
    # Heuristic: distance between current city and each city in cities
    # Edge cost: distance between current city and next city
    # Successor function: return all cities that are not visited
    
    frontier = PriorityQueue()
    frontier.put((0, startCity)) # .put((distance from last city, city object))

    cameFrom = [] # list of cities we have visited
    distSoFar = [] # distance traveled to each city

    #cameFrom.append(startCity)
    #distSoFar.append(0)
    
    while frontier:
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
                    # add city to frontier AKA priority queue
                    frontier.put((newCost, next))
    
    # calculate the distance of traveling back to our starting city
    distSoFar[-1] += distance(cameFrom[-1].latitude, cameFrom[-1].longitude, cameFrom[0].latitude, cameFrom[0].longitude)
    cameFrom.append(cameFrom[0])
                    
    return cameFrom, distSoFar

