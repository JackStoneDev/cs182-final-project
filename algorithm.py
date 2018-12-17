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

# Show initial map cost
SA_final = SimulatedAnnealing(3)
print 'Initial map cost: %d' % SA_final.cost(data_map)

# Plot initial map
plot = Plot()
plot.plot(data_map, False)

# Run simulated annealing experiments
for i in range(1, 5):
    print 'Running simulated annealing for type %d:' % i

    SA = SimulatedAnnealing(i)

    new_map = SA.anneal(data_map)
    print 'Cost: %d' % SA_final.cost(new_map)
    plot.plot(new_map, False, i)

# Run k-means
dropoff_zones = data_map.dropoff_zones.keys()
K = len(dropoff_zones)
locations = data_map.coordinates.keys()

k_means = KMeans(K, dropoff_zones, locations, data_map)

print 'Running k-means clustering:'
print 'Cost: %d' % k_means.run()
