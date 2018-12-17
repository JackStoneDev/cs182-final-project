import copy
import numpy as np
import matplotlib.pyplot as plt

# K-means clustering class
class KMeans:
    # Constructor
    def __init__(self, K, centers, points, data_map):
        self.K = K
        self.centers = centers
        self.points = points
        self.map = data_map
        self.max_distance = 10

        # Initialize empty list of clusters
        self.clusters = [[] for _ in range(K)]

    # Fits city locations to the K dropoff zones
    def fit(self):
        i = 0

        while True:
            # Make a copy of the previous centers
            previous_centers = copy.deepcopy(self.centers)

            # Initialize empty clusters list
            self.clusters = [[] for _ in range(self.K)]

            # Assign clusters and update centers
            self.assign_clusters()
            self.update_centers()

            # If no center assignments change then we are done
            if previous_centers == self.centers:
                break

            i += 1

    # Assigns city locations to dropoff zones
    def assign_clusters(self):
        # Loop through city locations
        for p in self.points:
            # Initialize min distance
            min_dist = float('inf')
            min_index = -1

            # Loop through dropoff zones
            for i in range(len(self.centers)):
                # Get dropoff zone
                c = self.centers[i]

                # Calculate distance from location to zone
                dist = np.linalg.norm(np.subtract(p, self.centers[i]))

                dist += (dist / self.max_distance) * self.map.coordinates[p]['population_density']

                # Take minimum distance
                if dist < min_dist:
                    min_dist = dist
                    min_index = i

            # Update clusters
            self.clusters[min_index].append(p)

    # Updates centers
    def update_centers(self):
        # Loop through dropoff zones
        for i in range(len(self.centers)):
            # Get points
            points = self.clusters[i]
            length = len(points)
            sum_x = 0
            sum_y = 0

            # Take average distance of points to center
            for p in points:
                sum_x += p[0]
                sum_y += p[1]

            self.centers[i] = (sum_x / length, sum_y / length)

    # Plots points
    def plot(self):
        plt.clf()

        # Set axis limits
        plt.xlim(0, self.map.map_size)
        plt.ylim(0, self.map.map_size)

        # Get x and y points
        x = []
        y = []
        colors = []

        # Scale color by population density
        for location in self.map.coordinates.keys():
            x.append(location[0])
            y.append(location[1])

            population_density = self.map.coordinates[location]['population_density']
            colors.append((0, 1.0, 0, population_density / self.map.max_population_density))

        # Plot city locations
        plt.scatter(x, y, color=colors)

        # Plot centers
        plt.scatter(zip(*self.centers)[0], zip(*self.centers)[1], c='r')
        plt.draw()
        plt.pause(5)

    # Runs k-means
    def run(self):
        self.plot()
        # Loop through clusters
        self.fit()
        self.plot()
