from map import Map
from simulated_annealing import SimulatedAnnealing
from plot import Plot
from k_means import KMeans

# Generate random map
data_map = Map(25)

# Add 20 random city points
for i in range(20):
    data_map.add_random_location()

# Add 5 random drop zones
for i in range(5):
    data_map.add_random_dropoff_zone()

averages = [0.0] * 6

num_iterations = 100
print 'Running simulated annealing and k-means clustering %d times' % num_iterations

for i in range(0, num_iterations):
    print 'Pass %d' % (i + 1)
    # Show initial map cost
    SA_final = SimulatedAnnealing(3)
    initial_map_cost = SA_final.cost(data_map)
    print 'Initial map cost: %d' % initial_map_cost
    averages[0] += initial_map_cost

    # Plot initial map
    plot = Plot()
    plot.plot(data_map, False)

    # Run simulated annealing experiments
    for i in range(1, 5):
        print 'Running simulated annealing for type %d:' % i

        SA = SimulatedAnnealing(i)

        new_map = SA.anneal(data_map)
        cost = SA_final.cost(new_map)
        print 'Cost: %d' % cost
        averages[i] += cost
        plot.plot(new_map, False, i)

    # Run k-means
    dropoff_zones = data_map.dropoff_zones.keys()
    K = len(dropoff_zones)
    locations = data_map.coordinates.keys()

    k_means = KMeans(K, dropoff_zones, locations, data_map)

    print 'Running k-means clustering:'
    kmeans_cost = k_means.run()
    print 'Cost: %d' % kmeans_cost
    averages[5] += kmeans_cost

# Print average costs
print map(lambda x: x / num_iterations, averages)
