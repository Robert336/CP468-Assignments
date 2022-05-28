


class City:
    def __init__(self, name, description, latitude, longitude):
        self.name = name
        self.description = description
        self.latitude = latitude
        self.longitude = longitude
        self.neighbors = [] # list of all cities

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)
    
    def __str__(self): # print city object (it will just print the name)
        return self.name
    
    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return (self.name == other.name and self.description == other.description and self.latitude == other.latitude and self.longitude == other.longitude)
    