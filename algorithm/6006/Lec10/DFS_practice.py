import networkx as nx
import matplotlib.pyplot as plt


# Defining a Class
class GraphVisualization:
    def __init__(self):
        # visual is a list which stores all
        # the set of edges that constitutes a
        # graph
        self.visual = []

    # addEdge function inputs the vertices of an
    # edge and appends it to the visual list
    def addEdge(self, a, b):
        temp = [a, b]
        self.visual.append(temp)

    # In visualize function G is an object of
    # class Graph given by networkx G.add_edges_from(visual)
    # creates a graph with a given list
    # nx.draw_networkx(G) - plots the graph
    # plt.show() - displays the graph
    def visualize(self):
        G = nx.Graph()
        G.add_edges_from(self.visual)
        nx.draw_networkx(G)
        plt.show()


# Driver code
G = GraphVisualization()

# test_graph = [
#     [1],
#     [0,2],
#     [1,3,4],
#     [2,5],
#     [2,5],
#     [3,4]
# ]
test_graph = [[1], [0, 2, 4], [1, 3], [2], [1]]
for i, item in enumerate(test_graph):
    for v in item:
        G.addEdge(i, v)


def dfs(Adj: list, s, parent=None, order=None):  # Adj adjacency list, s:start
    return


def full_dfs(Adj):
    return


print(f"{full_dfs(test_graph)=}")


G.visualize()
