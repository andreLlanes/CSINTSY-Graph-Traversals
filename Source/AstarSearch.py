import heapq
import matplotlib.pyplot as plt
import networkx as nx
from GraphUtility import calculate_heuristics, create_graph, pos, nodes
import time

class AstarSearch:
    def __init__(self):
        self.graph = create_graph()
        self.visiteds = set()

    # A* Search algorithm implementation
    def astar_search(self, start, goal):
        heuristics = calculate_heuristics(goal, pos)
        priority_queue = [(0 + heuristics[start], 0, start, [start])]
        while priority_queue:
            _, cumulative_cost, current_node, path = heapq.heappop(priority_queue)

            if current_node == goal:
                return path, cumulative_cost

            if current_node in self.visiteds:
                continue
            self.visiteds.add(current_node)
            print(f"Visited: {current_node}")

            # Explore neighbors
            for neighbor in self.graph.neighbors(current_node):
                if neighbor not in self.visiteds:
                    edge_weight = self.graph[current_node][neighbor]["weight"]
                    new_cost = cumulative_cost + edge_weight
                    new_path = path + [neighbor]
                    priority = new_cost + heuristics[neighbor]
                    heapq.heappush(
                        priority_queue, (priority, new_cost, neighbor, new_path)
                    )

        return None, float("inf")

    # Display A* result and return the path for visualization
    def display_astar_result(self, start, goal):
        start_time = time.time()  # Start timing
        path, total_cost = self.astar_search(start, goal)
        end_time = time.time()  # End timing
        
        execution_time = end_time - start_time  # Calculate execution time
        print(f"Execution time for A* search: {execution_time:.4f} seconds")
        
        if path:
            print(f"Path found: {' -> '.join(path)}")
            print(f"Total cost: {total_cost:.2f}")
            return path
        else:
            print(f"No path found from {start} to {goal}.")
            return None