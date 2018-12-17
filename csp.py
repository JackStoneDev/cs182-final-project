from map import Map
from simulated_annealing import SimulatedAnnealing
from k_means import KMeans

data_map = Map(25)

for i in range(20):
    data_map.add_random_location()

for i in range(5):
    data_map.add_random_dropoff_zone()

SA = SimulatedAnnealing()
SA.anneal(data_map)
dropoff_zones = data_map.dropoff_zones.keys()
K = len(dropoff_zones)
locations = data_map.coordinates.keys()

k_means = KMeans(K, dropoff_zones, locations, data_map)
k_means.run()
