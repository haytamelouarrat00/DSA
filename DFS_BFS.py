class Graph:

    def __init__(self, directed=False):
        self.is_directed = directed
        self.graph = {}
        self.node_weights = {}
        self.visited = []
        self.unvisited = {}
        self.distances = {}
        self.previous = {}

    def add_node(self, node, weight=1):
        self.graph[node] = {}
        self.node_weights[node] = weight

    def add_edge(self, start, end):
        self.graph[start][end] = True

        if not self.is_directed:
            self.graph[end][start] = True

    def get_neighbors(self, vertex):
        return list(self.graph.get(vertex, {}).keys())

    def get_weight(self, vertex):
        return self.graph[vertex]

    def get_successors(self, vertex):
        return list(self.graph.get(vertex, {}).keys())

    def get_predecessors(self, vertex):
        predecessors = []
        for v in self.graph:
            if vertex in self.graph[v]:
                predecessors.append(v)
        return predecessors

    def print_graph(self):
        print(self.graph)

    def BFS(self, start):
        queue = [start]
        processed = []
        while queue:
            vertex = queue.pop(0)
            if vertex not in processed:
                processed.append(vertex)
                queue.extend(self.get_successors(vertex))
                queue.sort()
        return processed


g = Graph(directed=True)
g.add_node('A', 5)
g.add_node('B', 10)
g.add_node('C', 7)
g.add_node('D', 3)
g.add_node('E', 2)
g.add_node('F', 1)

g.add_edge('A', 'B')
g.add_edge('B', 'C')
g.add_edge('B', 'E')
g.add_edge('A', 'D')
g.add_edge('D', 'F')

print(g.BFS('A'))

g.print_graph()
