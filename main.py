# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from src.DataStructures.Graph import Graph
  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    g = Graph(directed=True)
    g.add_node("A")
    g.add_node("B")
    g.add_node("C")

    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "C")
