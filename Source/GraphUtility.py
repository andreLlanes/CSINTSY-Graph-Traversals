import networkx as nx
import numpy as np

# Define positions for visualization
pos = {
    "A": (10, 10),
    "B": (9.5, 10),
    "C": (9.2, 9),
    "D": (6, 6),
    "E": (6.5, 10),
    "F": (6, 10),
    "G": (4.5, 10.2),
    "H": (4.5, 7),
    "I": (3.5, 9.7),
    "J1": (2.5, 9),
    "J2": (2, 6),
    "K": (1.5, 9.5),
    "L": (3, 8),
    "M": (2, 15),
    "N": (3, 15),
    "O": (6.5, 15),
    "P": (7.5, 14),
    "Q": (8, 14),
    "R": (9, 14),
    "S": (7, 17),
    "T": (10.7, 15),
    "U": (0.2, 8),
}

# List of nodes
nodes = list(pos.keys())

# List of edges with connections between nodes
edges = [
    ("A", "B"),
    ("B", "T"),
    ("B", "R"),
    ("B", "C"),
    ("C", "D"),
    ("D", "E"),
    ("D", "H"),
    ("E", "F"),
    ("E", "O"),
    ("F", "G"),
    ("F", "H"),
    ("G", "H"),
    ("G", "I"),
    ("H", "L"),
    ("I", "J1"),
    ("I", "N"),
    ("J1", "K"),
    ("J1", "L"),
    ("J2", "L"),
    ("J2", "U"),
    ("K", "U"),
    ("M", "N"),
    ("N", "O"),
    ("O", "P"),
    ("P", "S"),
    ("P", "Q"),
    ("Q", "R"),
    ("R", "T"),
]


# Function to calculate Euclidean distance between two points
def euclidean_distance(pos1, pos2):
    return np.sqrt((pos2[0] - pos1[0]) ** 2 + (pos2[1] - pos1[1]) ** 2)


def calculate_heuristics(goal, pos):
    goal_pos = pos[goal]
    heuristics = {node: euclidean_distance(pos[node], goal_pos) for node in pos}
    
    for node, heuristic in heuristics.items():
        print(f"Node: {node}, Heuristic: {heuristic:.2f}")
    
    return heuristics


# Function to create and initialize the graph with positions and edge weights
def create_graph():
    Gn = nx.Graph()
    for edge in edges:
        node1, node2 = edge
        distance = euclidean_distance(pos[node1], pos[node2])
        Gn.add_edge(node1, node2, weight=distance)
    return Gn