"""
This algorithm allows the user to add vertices and edges to a graph,
then find the shortest path between two given vertices.
"""
from heapq import heappop, heappush


class Djikstra:
    def __init__(self, directed=False, weighted=False):
        self.is_directed = directed
        self.is_weighted = weighted
        self.graph = {}
        self.visited = []
        self.unvisited = []
        self.distances = {}
        self.previous = {}

    def add_vertex(self, vertex):
        self.graph[vertex] = {}

    def add_edge(self, vertex1, vertex2, weight1_2=None, weight2_1=None):
        if self.is_weighted and self.is_directed:
            self.graph[vertex1][vertex2] = weight1_2
            self.graph[vertex2][vertex1] = weight2_1
        elif self.is_weighted:
            self.graph[vertex1][vertex2] = weight1_2
            self.graph[vertex2][vertex1] = weight1_2
        else:
            self.graph[vertex1][vertex2] = 1
            self.graph[vertex2][vertex1] = 1

    def get_neighbors(self, vertex):
        return list(self.graph.get(vertex, {}).keys())

    def get_distance(self, vertex1, vertex2):
        if vertex1 in self.get_neighbors(vertex2):
            return self.graph[vertex1][vertex2]
        else:
            # raise ValueError(f'Vertex {vertex2} is not a neighbor of {vertex1}')
            return 0

    def find_shortest_path(self, start, end):
        if start not in self.graph or end not in self.graph:
            raise ValueError(f'Vertex {start} or {end} not in graph')

        # Initialization
        self.unvisited = list(self.graph.keys())
        distances = {vertex: float('inf') for vertex in self.unvisited}
        previous_nodes = {vertex: None for vertex in self.unvisited}
        distances[start] = 0

        # Priority queue to efficiently get the minimum distance vertex
        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_vertex = heappop(priority_queue)

            # Update distances and previous_nodes for neighbors
            for neighbor in self.get_neighbors(current_vertex):
                #print("Checking neighbor:", neighbor + " from vertex:", current_vertex)
                new_distance = current_distance + (self.get_distance(current_vertex, neighbor)
                                                   if self.get_distance(current_vertex, neighbor) is not None else 0)
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous_nodes[neighbor] = current_vertex
                    heappush(priority_queue, (new_distance, neighbor))

        # Check if end vertex is reachable
        if distances[end] == float('inf'):
            return float('inf'), []

        # Reconstruct the shortest path
        shortest_path = []
        current_node = end
        while current_node is not None:
            shortest_path.insert(0, current_node)
            current_node = previous_nodes[current_node]

        return distances[end], shortest_path

    def __str__(self):
        return str(self.graph)

    def print_graph(self):
        for vertex, neighbors in self.graph.items():
            print(f"Node {vertex}:")
            if neighbors:
                for neighbor, weight in neighbors.items():
                    if self.is_weighted:
                        print(f"  -> Edge to {neighbor} (Weight: {weight})")
                    else:
                        print(f"  -> Edge to {neighbor}")
            else:
                print("  -> No outgoing edges")


# Test Case 1: Basic Unweighted Graph
print("Test Case 1: Basic Unweighted Graph")
graph1 = Djikstra()
graph1.add_vertex("A")
graph1.add_vertex("B")
graph1.add_vertex("C")
graph1.add_edge("A", "B", 2)
graph1.add_edge("B", "C", 1)
print(graph1.find_shortest_path("A", "C"))  # Output should be (2, ['A', 'B', 'C'])

# Test Case 2: Weighted Graph
print("Test Case 2: Weighted Graph")
graph2 = Djikstra(weighted=True)
graph2.add_vertex("A")
graph2.add_vertex("B")
graph2.add_vertex("C")
graph2.add_edge("A", "B", 2)
graph2.add_edge("B", "C", 3)
print(graph2.find_shortest_path("A", "C"))  # Output should be (5, ['A', 'B', 'C'])

# Test Case 3: Directed Weighted Graph
print("Test Case 3: Directed Weighted Graph")
graph3 = Djikstra(directed=True, weighted=True)
graph3.add_vertex("A")
graph3.add_vertex("B")
graph3.add_vertex("C")
graph3.add_edge("A", "B", 2)
graph3.add_edge("B", "C", 3)
print(graph3.find_shortest_path("A", "C"))  # Output should be (5, ['A', 'B', 'C'])

# Test Case 4: Unweighted Graph with Isolated Node
print("Test Case 4: Unweighted Graph with Isolated Node")
graph4 = Djikstra()
graph4.add_vertex("A")
graph4.add_vertex("B")
graph4.add_vertex("C")
graph4.add_vertex("D")
print(graph4.find_shortest_path("A", "D"))  # Output should be (0, ['A', 'D'])

# Test Case 5: Unweighted Graph with Disconnected Components
print("Test Case 5: Unweighted Graph with Disconnected Components")
graph5 = Djikstra()
graph5.add_vertex("A")
graph5.add_vertex("B")
graph5.add_vertex("C")
graph5.add_vertex("D")
graph5.add_edge("A", "B")
graph5.add_edge("C", "D")
print(graph5.find_shortest_path("A", "D"))  # Output should be (0, ['A', 'D'])
