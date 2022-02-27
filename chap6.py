# BREADTH-FIRST SEARCH, GRAPHS
from collections import deque

# graph = {
#     "washington": ["oregon", "montana"],
#     "montana": [],
#     "oregon": ["utah", "colorado"],
#     "utah": ["colorado"],
#     "colorado": ["nevada"],
#     "nevada": ["california", "mexico"],
#     "california": ["mexico", "central_america"],
#     "mexico": ["texas"],
#     "texas": ["central_america"],
#     "central_america": ["peru"],
#     "peru": ["chile"],
#     "chile": ["vene"],
#     "vene": ["chile"],
# }


# def graph_search(graph, from_):  # dumb example from book
#     search_queue = deque()
#     search_queue += graph[from_]
#     while search_queue:
#         node = search_queue.popleft()
#         print(node)
#         if place_ends_with_m(node):
#             print(f"Found {node}")
#             return True
#         else:
#             search_queue += graph[node]
#     return False


# def place_ends_with_m(place):
#     return place[-1] == "m"


# graph_search(graph, "washington")


graph = {  # I know this is not geographically correct...
    "washington": ["oregon", "montana"],
    "montana": [],
    "oregon": ["utah", "colorado"],
    "utah": ["colorado"],
    "colorado": ["nevada"],
    "nevada": ["california", "mexico"],
    "california": ["mexico", "central_america"],
    "mexico": ["texas"],
    "texas": ["central_america"],
    "central_america": ["peru"],
    "peru": ["chile"],
    "chile": ["vene"],
    "vene": [],
    "germany": [],
}


def graph_search(graph, from_, to):  # my example to find a path from one place to another
    path = [from_]
    search_queue = graph.get(from_)
    while search_queue:
        node = search_queue.pop(0)
        if node == to:
            location = [node]
        else:
            location = graph_search(graph, node, to)
        return path + location
    raise Exception(f"Could not find location {to} from starting location.")


graph_search(graph, "washington", "peru")
