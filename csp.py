from map import Map
from simulated_annealing import SimulatedAnnealing

data_map = Map(1000)

for i in range(5):
    data_map.add_random_location()

SA = SimulatedAnnealing()
SA.anneal(data_map)
