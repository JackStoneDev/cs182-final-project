import random
import numpy as np
import math
from plot import Plot

# Simulated annealing class
class SimulatedAnnealing:
    max_distance = 10

    # Calculates "cost" of a particular map by taking the average over all locations of minimum distance to another node
    def cost(self, map):
        # Get all dropoff zones of map
        dropoff_zones = map.dropoff_zones.keys()

        # Get all locations on the map
        coordinates = map.coordinates.keys()

        # Get the number of locations that we have and initialize a sum to take the average later
        num_coordinates = len(coordinates)
        sum = 0.0

        # Loop through locations on map
        for location in coordinates:
            # Initialize minimum distance
            min_distance = float('inf')

            # Loop through dropoff zones
            for zone in dropoff_zones:
                # If the neighbor is the same point, then skip
                if location == zone:
                    continue

                # Calculate Euclidean distance to neighbor
                distance = np.linalg.norm(np.subtract(location, zone))

                # Minimize over all distances
                min_distance = min(min_distance, distance)

            # Add minimum distance to sum
            sum += min_distance + (min_distance / self.max_distance) * map.coordinates[location]['population_density']

        # Return average of distances
        return sum / num_coordinates

    # Generates neighboring state of given map by randomly moving dropoff zones around until all locations are within an arbitrary distance from a dropoff zone
    def neighbor(self, map):
        # Check if all locations are within an arbitrary distance of a dropoff zone
        all_within_distance = False

        while not all_within_distance:
            all_within_distance = True

            # Swap a random dropoff zone in the map
            random_dropoff_zone = random.choice(map.dropoff_zones.keys())
            del map.dropoff_zones[random_dropoff_zone]
            map.add_random_dropoff_zone()

            # Get all coordinates of map
            coordinates = map.coordinates.keys()

            # Get all dropoff zones of map
            dropoff_zones = map.dropoff_zones.keys()

            # Loop through coordinates
            for location in coordinates:
                # Initialize minimum distance
                min_distance = float('inf')

                # Track if the location is within an arbitrary distance from a dropoff zone
                location_within_distance = False

                # Loop through neighbors
                for zone in dropoff_zones:
                    # If the neighbor is the same point, then skip
                    if location == zone:
                        continue

                    # Calculate Euclidean distance to neighbor
                    distance = np.linalg.norm(np.subtract(location, zone))

                    # Is this distance within the arbitrary distance?
                    if distance <= self.max_distance:
                        location_within_distance = True
                        break

                # If this location is not within the distance, then we must make another swap in the graph
                if not location_within_distance:
                    all_within_distance = False
                    break

        return map

    # Calculates acceptance probability for a new map solution
    def acceptance_probability(self, old_cost, new_cost, T):
        return math.exp((new_cost - old_cost) / T)

    # Performs simulated annealing on a city map
    def anneal(self, map):
        # Plot old map
        plot = Plot()
        plot.plot(map)

        # Get cost of the input
        old_cost = self.cost(map)

        # Initialize annealing values
        T = 1.0
        T_min = 0.01
        alpha = 0.9

        # Iterate until we hit the max number of iterations
        while T > T_min:
            i = 1

            # Generate 100 unique neighbors
            while i <= 100:
                new_map = self.neighbor(map)

                new_cost = self.cost(new_map)
                ap = self.acceptance_probability(old_cost, new_cost, T)

                # If new solution is accepted then we update
                if ap > random.random():
                    map.dropoff_zones = new_map.dropoff_zones
                    old_cost = new_cost

                i += 1

            T *= alpha

        # Plot new map
        plot.plot(new_map, False)

        return map
