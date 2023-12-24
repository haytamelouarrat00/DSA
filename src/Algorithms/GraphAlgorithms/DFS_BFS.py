from Graph import *


def BFS(Grph, start):
    queue = [start]
    processed = []
    while queue:
        vertex = queue.pop(0)
        if vertex not in processed:
            processed.append(vertex)
            queue.extend(neighbor for neighbor in Grph.get_neighbors(vertex) if neighbor not in processed)

    return processed


def DFS(Grph, start):
    stack = [start]
    processed = []
    while stack:
        vertex = stack.pop()
        if vertex not in processed:
            processed.append(vertex)
            stack.extend(neighbor for neighbor in Grph.get_neighbors(vertex) if neighbor not in processed)

    return processed


# Create a directed graph
graph_directed = Graph(directed=True)

# Add nodes with weights
graph_directed.add_node('A', 5)
graph_directed.add_node('B', 10)
graph_directed.add_node('C', 7)
graph_directed.add_node('D', 3)
graph_directed.add_node('E', 2)
graph_directed.add_node('F', 1)

# Add edges
graph_directed.add_edge('A', 'B')
graph_directed.add_edge('B', 'C')
graph_directed.add_edge('B', 'E')
graph_directed.add_edge('A', 'D')
graph_directed.add_edge('D', 'F')

"""
        A
       / \
      B   D
     / \   \
    C   E   F
"""

# Test BFS on directed graph
print(BFS(graph_directed, 'A'))
# Expected output: ['A', 'B', 'D', 'C', 'E', 'F']

# Create an undirected graph
graph_undirected = Graph(directed=False)

# Add nodes with weights
graph_undirected.add_node('X', 3)
graph_undirected.add_node('Y', 8)
graph_undirected.add_node('Z', 4)

# Add edges
graph_undirected.add_edge('X', 'Y')
graph_undirected.add_edge('Y', 'Z')

"""
    X
    |
    Y
    |
    Z
"""
# Test BFS on undirected graph
print(BFS(graph_undirected, 'X'))
# Expected output: ['X', 'Y', 'Z']

# Test DFS on directed graph
print(DFS(graph_directed, 'A'))
# Expected output: ['A', 'D', 'F', 'B', 'E', 'C']

# Test DFS on undirected graph
print(DFS(graph_undirected, 'X'))
# Expected output: ['X', 'Y', 'Z']
