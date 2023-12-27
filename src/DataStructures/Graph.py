class Graph:
    def __init__(self, directed=False):
        self.is_directed = directed
        self.graph = {}
        self.node_weights = {}
        self.visited = {}

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
        return self.node_weights[vertex]

    def print_graph(self):
        print(self.graph)