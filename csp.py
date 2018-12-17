from map import Map
from simulated_annealing import SimulatedAnnealing
from k_means import KMeans

data_map = Map(25)

for i in range(20):
    data_map.add_random_location()

for i in range(5):
    data_map.add_random_dropoff_zone()

SA_final = SimulatedAnnealing(3)
print 'Initial map cost: %d' % SA_final.cost(data_map)

for i in range(1, 5):
    print 'Running simulated annealing for type %d:' % i

    SA = SimulatedAnnealing(i)
    print 'Cost: %d' % SA_final.cost(SA.anneal(data_map))

dropoff_zones = data_map.dropoff_zones.keys()
K = len(dropoff_zones)
locations = data_map.coordinates.keys()

k_means = KMeans(K, dropoff_zones, locations, data_map)
k_means.run()
