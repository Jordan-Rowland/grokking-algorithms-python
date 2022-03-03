# GREEDY ALGORITHMS

states_needed = set("""mt wa or id nv ut ca az""".split())

stations = {
    "kone": set("""id nv ut""".split()),
    "ktwo": set("""wa id mt""".split()),
    "kthree": set("""or nv mt""".split()),
    "kfour": set("""nv ut""".split()),
    "kfive": set("""ca az""".split()),
}

final_stations = set()

while states_needed:
    best_station = None
    states_covered = set()
    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
            final_stations.add(best_station)
            states_needed -= states_covered

final_stations

