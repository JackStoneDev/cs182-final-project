import random
import numpy as np

# Simulated annealing class
class SimulatedAnnealing:
    max_distance = 40

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

    # Generates neighboring state of given map by randomly moving locations around until all locations are within an arbitrary distance from one another
    def neighbor(self, map):
        # Check if all locations are within an arbitrary distance of another location
        all_within_distance = False

        while not all_within_distance:
            all_within_distance = True

            # Swap a random location in the map
            random_location = random.choice(map.coordinates.keys())
            del map.coordinates[random_location]
            map.add_random_location()

            # Get all coordinates of map
            coordinates = map.coordinates.keys()

            # Loop through coordinates
            for location in coordinates:
                # Initialize minimum distance
                min_distance = float('inf')

                # Track if the location is within an arbitrary distance from any other node
                location_within_distance = False

                # Loop through neighbors
                for neighbor in coordinates:
                    # If the neighbor is the same point, then skip
                    if location == neighbor:
                        continue

                    # Calculate Euclidean distance to neighbor
                    distance = np.linalg.norm(np.subtract(location, neighbor))

                    # Is this distance within the arbitrary distance?
                    if distance <= self.max_distance:
                        location_within_distance = True
                        break

                # If this location is not within the distance, then we must make another swap in the graph
                if not location_within_distance:
                    all_within_distance = False
                    break

        return map
