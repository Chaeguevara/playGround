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
    if parent is None:  # O(1)
        parent = [None] * len(Adj)  # O(v)
        parent[s] = s  # O(1)
        order = []  # O(1)
    for v in Adj[s]:  # O(Adj[s])
        if parent[v] is None:  # O(1)
            parent[v] = s  # O(1)
            dfs(Adj, v, parent, order)  # recursion
    order.append(s)  # last node will come first O(1) amortized
    return parent, order


def full_dfs(Adj):
    parent = [None] * len(Adj)  # O(V)
    order = []  # O(1)
    for v in range(len(Adj)):  # O(V)
        if parent[v] is None:  # O(1)
            parent[v] = v  # O(1)
            dfs(Adj, v, parent, order)
    return parent, order


def full_xxx(Adj,f):
    parent = [None] * len(Adj)  # O(V)
    order = []  # O(1)
    for v in range(len(Adj)):  # O(V)
        if parent[v] is None:  # O(1)
            parent[v] = v  # O(1)
            f(Adj, v, parent, order)
    return parent, order

def full_xxx_by_def(f):
    def full_something(Adj):
        parent = [None] * len(Adj)  # O(V)
        order = []  # O(1)
        for v in range(len(Adj)):  # O(V)
            if parent[v] is None:  # O(1)
                parent[v] = v  # O(1)
                f(Adj, v, parent, order)
        return parent, order
    return full_something

full_scan_by_lambda = lambda adj: full_xxx(adj,dfs)
full_scan_by_def = full_xxx_by_def(dfs)


print(f"{full_dfs(test_graph)=}")
print(f"{full_scan_by_lambda(test_graph)=}")
print(f"{full_scan_by_def(test_graph)=}")


G.visualize()
