# Map class
class Map:
    # Constructor
    def __init__(self):
        # Initialize coordinates to empty dictionary
        self.coordinates = {}

    # Adds location to the map
    # Takes x, y coordinates, boolean representing road or not, and population density as number
    def add(self, coordinates, road, population_density):
        self.coordinates[coordinates] = {
            'road': road,
            'population_density': population_density
        }
