from map import Map

data_map = Map(1000)

for i in range(100):
    data_map.add_random_location()

print data_map.coordinates
