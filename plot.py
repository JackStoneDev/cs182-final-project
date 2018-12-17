import matplotlib.pyplot as plt

# Graph plotting class
class Plot:
    # Plots city map
    def plot(self, map, should_pause=True, type=0):
        # Clear all previous points
        plt.clf()

        # Set axis limits
        plt.xlim(0, map.map_size)
        plt.ylim(0, map.map_size)

        # Get x and y points
        x = []
        y = []
        colors = []

        # Scale color by population density then plot
        for location in map.coordinates.keys():
            x.append(location[0])
            y.append(location[1])

            population_density = map.coordinates[location]['population_density']
            colors.append((0, 1.0, 0, population_density / map.max_population_density))

        # Plot city locations
        plt.scatter(x, y, color=colors)

        # Break up x and y coordinates into their own list
        x, y = zip(*map.dropoff_zones)
        x = list(x)
        y = list(y)

        # Plot dropoff zones
        plt.scatter(x, y, c='r')

        plt.savefig('results/simulated_annealing_%d.png' % type)
