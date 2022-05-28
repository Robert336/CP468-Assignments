


class City:
    def __init__(self, name, description, latitude, longitude):
        self.name = name
        self.description = description
        self.latitude = latitude
        self.longitude = longitude
        self.visited = False
        self.neighbors = []
        self.items = []

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)
    


    def __str__(self):
        return self.name;