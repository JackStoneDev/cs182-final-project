from map import Map
from simulated_annealing import SimulatedAnnealing

data_map = Map(100)

for i in range(100):
    data_map.add_random_location()

for i in range(5):
    data_map.add_random_dropoff_zone()

SA = SimulatedAnnealing()
SA.anneal(data_map)
