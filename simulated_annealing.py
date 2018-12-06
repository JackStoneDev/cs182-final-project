from random import random
import numpy as np

# Simulated annealing class
class SimulatedAnnealing:
    max_dist = 10

    # Calculates "cost" of a particular map by taking the average over all locations of minimum distance to another node
    def cost(self, map):
        # Get all coordinates of map
        coordinates = map.coordinates.keys()

        # Get the number of coordinates that we have and initialize a sum to take the average later
        num_coordinates = len(coordinates)
        sum = 0.0

        # Loop through coordinates
        for location in coordinates:
            # Initialize minimum distance
            min_distance = float('inf')

            # Loop through neighbors
            for neighbor in coordinates:
                # If the neighbor is the same point, then skip
                if location == neighbor:
                    continue

                # Calculate Euclidean distance to neighbor
                distance = np.linalg.norm(np.subtract(location, neighbor))

                # Minimize over all distances
                min_distance = min(min_distance, distance)

            # Add minimum distance to sum
            sum += min_distance

        # Return average of distances
        return sum / num_coordinates
