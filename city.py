


class City:
    def __init__(self, name, description, latitude, longitude):
        self.name = name
        self.description = description
        self.latitude = latitude
        self.longitude = longitude
        self.visited = False
        self.neighbors = [] # list of neighboring cities (idk if we need this)

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)
    
    def __str__(self): # print city object (it will just print the name)
        return self.name;