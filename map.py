import random

# Map class
class Map:
    # Constant for maximum population density allowed
    max_population_density = 100000

    # Constructor
    # Accepts size of N x N map
    def __init__(self, map_size):
        # Initialize coordinates to empty dictionary
        self.coordinates = {}
        self.map_size = map_size

    # Adds location to the map
    # Takes x, y coordinates, boolean representing road or not, and population density as number
    def add(self, coordinates, road, population_density):
        self.coordinates[coordinates] = {
            'road': road,
            'population_density': population_density
        }

    # Adds a random location to the map within the confines of map_size
    def add_random_location(self):
        # Randomize location details
        x = random.uniform(0.0, self.map_size)
        y = random.uniform(0.0, self.map_size)
        coordinates = (x, y)
        road = random.choice([True, False])
        population_density = random.uniform(1.0, self.max_population_density)

        self.add(coordinates, road, population_density)
