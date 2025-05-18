import matplotlib.pyplot as plt
import networkx as nx
from GraphUtility import pos


# Get user input for the start and goal nodes
def get_user_input(nodes):
    print("Available nodes:", ", ".join(nodes))
    start_node = input("Enter the start node: ").strip().upper()
    goal_node = input("Enter the goal node: ").strip().upper()

    if start_node not in nodes or goal_node not in nodes:
        print("Invalid input! Please enter valid nodes.")
        return get_user_input(nodes)  # Retry input
    return start_node, goal_node


# Visualize the graph with node positions and optionally highlight a path
def visualize_graph(graph, path=None):
    plt.figure(figsize=(10, 10))

    # Draw nodes and edges
    nx.draw(
        graph,
        pos,
        with_labels=True,
        node_color="green",
        font_size=10,
        font_color="white",
    )

    # Get edge labels (weights) to display on the graph
    edge_labels = nx.get_edge_attributes(graph, "weight")
    edge_labels = {key: f"{value:.2f}" for key, value in edge_labels.items()}
    nx.draw_networkx_edge_labels(
        graph, pos, edge_labels=edge_labels, font_color="green"
    )

    # Highlight the path found by UCS, if any
    if path:
        path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
        nx.draw_networkx_edges(graph, pos, edgelist=path_edges, width=3, edge_color="r")

    plt.show()