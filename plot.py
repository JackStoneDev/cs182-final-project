import matplotlib.pyplot as plt

# Graph plotting class
class Plot:
    # Plots city map
    def plot(self, map, should_pause=True):
        # Clear all previous points
        plt.clf()

        # Set axis limits
        plt.xlim(0, map.map_size)
        plt.ylim(0, map.map_size)

        # Break up x and y coordinates into their own list
        x, y = zip(*map.coordinates)
        x = list(x)
        y = list(y)

        # Plot locations
        plt.scatter(x, y, c='g')

        # Break up x and y coordinates into their own list
        x, y = zip(*map.dropoff_zones)
        x = list(x)
        y = list(y)

        # Plot dropoff zones
        plt.scatter(x, y, c='r')

        # Show plot
        plt.draw()

        # Are we continuing with the graph display?
        if should_pause:
            plt.pause(0.0001)
        else:
            plt.pause(10000)
