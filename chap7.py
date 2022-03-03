# DIJKSTRA'S ALGORITHM

from math import inf


# weighted graph
# graph = {
#     "book": [
#         {"node": "lp", "weight": 5},
#         {"node": "poster", "weight": 0},
#     ],
#     "lp": [
#         {"node": "guitar", "weight": 15},
#         {"node": "drums", "weight": 20},
#     ],
#     "poster": [
#         {"node": "guitar", "weight": 30},
#         {"node": "drums", "weight": 35},
#     ],
#     "guitar": [
#         {"node": "piano", "weight": 10},
#     ],
#     "drums": [
#         {"node": "piano", "weight": 20},
#     ],
#     "piano": [],
# }

# def dijkstras_algo(graph, from_, to):
    # pass
# dijkstras_algo(graph, "book", "piano")


graph = {
    "start": {"a": 6, "b": 2},
    "a": {"finish": 1},
    "b": {"a": 3, "finish": 5},
    "finish": None,
}

costs = {
    "a": 6,
    "b": 2,
    "finish": inf,
}

parents = {
    "a": "start",
    "b": "start",
    "finish": None,
}

processed = []

def dijkstras_algo(graph):
    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbours = graph[node]
        for n, cost in neighbours.items():
            new_cost = cost + neighbours[n]
            print(new_cost)
            print(cost)
            print(n)
            if new_cost < cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        print(costs)
        node = find_lowest_cost_node(costs)


def find_lowest_cost_node(costs):
    lowest = inf
    lowest_key = None
    for node, cost in costs.items():
        if cost < lowest and node not in processed:
            lowest = cost
            lowest_key = node
    print("returning -> ", lowest_key)
    return lowest_key


find_lowest_cost_node(costs)

dijkstras_algo(graph)
