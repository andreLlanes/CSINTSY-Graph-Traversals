import heapq
from GraphUtility import create_graph
import time

class UniformCostSearch:
    def __init__(self):
        self.graph = create_graph()
        self.visited = set()

    # Uniform Cost Search (UCS) algorithm implementation
    def uniform_cost_search(self, start, goal):
        priority_queue = [(0, start, [start])]

        while priority_queue:
            cumulative_cost, current_node, path = heapq.heappop(priority_queue)

            if current_node == goal:
                return path, cumulative_cost

            if current_node in self.visited:
                continue
            self.visited.add(current_node)
            print(f"Visited: {current_node}")
            # Explore neighbors
            for neighbor in self.graph.neighbors(current_node):
                if neighbor not in self.visited:
                    edge_weight = self.graph[current_node][neighbor]["weight"]
                    new_cost = cumulative_cost + edge_weight
                    new_path = path + [neighbor]
                    heapq.heappush(priority_queue, (new_cost, neighbor, new_path))
        
        return None, float("inf")

    # Display UCS result and return the path for visualization    
    def display_result(self, start, goal):
        start_time = time.time()  # Start timing
        path, total_cost = self.uniform_cost_search(start, goal)
        end_time = time.time()  # End timing
        
        execution_time = end_time - start_time  # Calculate execution time
        print(f"Execution time for UCS search: {execution_time:.4f} seconds")
        
        if path:
            print(f"Path found: {' -> '.join(path)}")
            print(f"Total cost: {total_cost:.2f}")
            return path
        else:
            print(f"No path found from {start} to {goal}.")
            return None