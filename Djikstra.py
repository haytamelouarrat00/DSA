"""
This algorithm allows the user to add vertices and edges to a graph,
then find the shortest path between two given vertices.
"""


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
        if self.is_weighted:
            if vertex1 in self.get_neighbors(vertex2):
                return self.graph[vertex1][vertex2]
            else:
                # raise ValueError(f'Vertex {vertex2} is not a neighbor of {vertex1}')
                return 0

    def find_shortest_path(self, start, end):
        if self.is_weighted:
            self.unvisited = list(self.graph.keys())
            neighbors = self.get_neighbors(start)
            dictdist = {start: 0}
            for vertex in self.unvisited:
                if vertex != start:
                    dictdist[vertex] = float('inf')
            for neighbor in neighbors:
                dictdist[neighbor] = self.get_distance(start, neighbor)

            self.visited.append(start)
            self.unvisited.remove(start)
            while self.unvisited:
                minvertex = min(self.unvisited, key=dictdist.get)
                self.visited.append(minvertex)
                self.unvisited.remove(minvertex)
                for neighbor in self.get_neighbors(minvertex):
                    if neighbor in self.unvisited:
                        if dictdist[minvertex] + self.get_distance(minvertex, neighbor) < dictdist[neighbor]:
                            dictdist[neighbor] = dictdist[minvertex] + self.get_distance(minvertex, neighbor)
                print(dictdist)

    def __str__(self):
        return str(self.graph)

    def print_graph(self):
        for vertex, neighbors in self.graph.items():
            print(f"{vertex}:")
            for neighbor, weight in neighbors.items():
                print(f"  -> {neighbor}{' (Weight: ' + str(weight) + ')' if self.is_weighted else ''}")


# Test Case 1: Unweighted, Undirected Graph
print("Test Case 1:")
d = Djikstra(directed=False, weighted=True)
d.add_vertex('A')
d.add_vertex('B')
d.add_vertex('C')
d.add_vertex('D')
d.add_vertex('E')
d.add_vertex('F')
d.add_vertex('G')

d.add_edge('A', 'B', 5)
d.add_edge('A', 'C', 1)
d.add_edge('B', 'C', 7)
d.add_edge('C', 'D', 3)
d.add_edge('D', 'E', 1)
d.add_edge('D', 'F', 4)
d.add_edge('E', 'F', 2)
d.add_edge('E', 'B', 8)
d.add_edge('C', 'F', 6)
d.add_edge('G', 'A', 3)
d.add_edge('G', 'D', 1)
d.add_edge('A', 'G', -2)

d.print_graph()
d.find_shortest_path('A', 'D')
print("\n")

"""# Test Case 2: Weighted, Directed Graph
print("Test Case 2:")
d = Djikstra(directed=True, weighted=True)
d.add_vertex('X')
d.add_vertex('Y')
d.add_vertex('Z')
d.add_vertex('W')

d.add_edge('X', 'Y', 5, 1 / 5)
d.add_edge('Y', 'Z', 3, 1 / 3)
d.add_edge('Z', 'W', 2, 1 / 2)

d.print_graph()
d.find_shortest_path('X', 'W')
print("\n")

# Test Case 3: Weighted, Undirected Graph
print("Test Case 3:")
d = Djikstra(directed=False, weighted=True)
d.add_vertex('P')
d.add_vertex('Q')
d.add_vertex('R')
d.add_vertex('S')

d.add_edge('P', 'Q', 4, 1 / 4)
d.add_edge('Q', 'R', 2, 1 / 2)
d.add_edge('R', 'S', 3, 1 / 3)

d.print_graph()
d.find_shortest_path('P', 'S')
print("\n")

# Test Case 4: Directed, Unweighted Graph
print("Test Case 4:")
d = Djikstra(directed=True, weighted=False)
d.add_vertex('M')
d.add_vertex('N')
d.add_vertex('O')
d.add_vertex('P')

d.add_edge('M', 'N')
d.add_edge('N', 'O')
d.add_edge('O', 'P')

d.print_graph()
d.find_shortest_path('M', 'P')
print("\n")

# Test Case 5: Weighted, Directed Graph (provided example)
print("Test Case 5 (Provided Example):")
d = Djikstra(directed=True, weighted=True)
d.add_vertex('USD')
d.add_vertex('GBP')
d.add_vertex('JPY')
d.add_vertex('AUD')

d.add_edge('USD', 'JPY', 110, 1 / 110)
d.add_edge('USD', 'AUD', 1.45, 1 / 1.45)
d.add_edge('JPY', 'GBP', 0.0070, 1 / 0.0070)

d.print_graph()
d.find_shortest_path('AUD', 'GBP')
"""
