import tkinter as tk
from tkinter import messagebox
import UniformCostSearch
import AstarSearch
from InputVisualization import visualize_graph, get_user_input
from GraphUtility import nodes  # List of available nodes


class PathFinding:
    def __init__(self, root):
        self.root = root
        self.root.title("Pathfinding GUI")

        # Labels for the GUI
        tk.Label(root, text="Start Node:").grid(row=0, column=0)
        tk.Label(root, text="End Node:").grid(row=1, column=0)
        tk.Label(root, text="Algorithm:").grid(row=2, column=0)

        # Dropdown menu for start and end node selection
        self.start_node = tk.StringVar(root)
        self.end_node = tk.StringVar(root)
        self.algorithm_choice = tk.StringVar(root)

        # Initialize dropdown options (nodes)
        self.start_node.set(nodes[0])  # Default value
        self.end_node.set(nodes[0])  # Default value

        # Dropdown menus for start, end nodes, and algorithm choice
        self.start_menu = tk.OptionMenu(root, self.start_node, *nodes)
        self.start_menu.grid(row=0, column=1)

        self.end_menu = tk.OptionMenu(root, self.end_node, *nodes)
        self.end_menu.grid(row=1, column=1)

        # Algorithm selection (UCS or A*)
        self.algorithm_menu = tk.OptionMenu(root, self.algorithm_choice, "UCS", "A*")
        self.algorithm_choice.set("UCS")  # Default value
        self.algorithm_menu.grid(row=2, column=1)

        # Button to start the search
        self.search_button = tk.Button(
            root, text="Start Search", command=self.start_search
        )
        self.search_button.grid(row=3, columnspan=2)

    def start_search(self):
        start_node = self.start_node.get()
        end_node = self.end_node.get()
        algorithm = self.algorithm_choice.get()

        if algorithm == "UCS":
            self.run_ucs(start_node, end_node)
        elif algorithm == "A*":
            self.run_astar(start_node, end_node)
        else:
            messagebox.showerror("Algorithm Error", "Invalid algorithm selected.")

    def run_ucs(self, start, goal):
        ucs = UniformCostSearch.UniformCostSearch()
        path = ucs.display_result(start, goal)
        if path:
            visualize_graph(ucs.graph, path)

    def run_astar(self, start, goal):
        astar = AstarSearch.AstarSearch()
        path = astar.display_astar_result(start, goal)
        if path:
            visualize_graph(astar.graph, path)