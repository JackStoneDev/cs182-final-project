import matplotlib.pyplot as plt

# Graph plotting class
class Plot:
    # Plots city map
    def plot(self, map):
        # Clear all previous points
        plt.clf()

        # Break up x and y coordinates into their own list
        x, y = zip(*map.coordinates)
        x = list(x)
        y = list(y)

        # Plot points
        for location in map.coordinates:
            plt.scatter(x, y)

        # Show plot
        plt.draw()
        plt.pause(0.0001)
