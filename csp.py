from map import Map
from simulated_annealing import SimulatedAnnealing

data_map = Map(30)

for i in range(20):
    data_map.add_random_location()

for i in range(5):
    data_map.add_random_dropoff_zone()

SA = SimulatedAnnealing()
SA.anneal(data_map)
