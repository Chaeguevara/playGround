from DAG_Relaxation import dfs, try_to_relax
import networkx as nx
import matplotlib.pyplot as plt
import random

# Defining a Class
class GraphVisualizer:
    def __init__(self, adjacency_list, weights):
        self.adjacency_list = adjacency_list
        self.weights = weights
        self.graph = nx.DiGraph()
        self.create_graph()

    def create_graph(self):
        for u, neighbors in enumerate(self.adjacency_list):
            for v in neighbors:
                weight = self.weights.get((u, v), 0)
                self.graph.add_edge(u, v, weight=weight)

    def draw_graph(self):
        pos = nx.spring_layout(self.graph)  # positions for all nodes
        edge_labels = {(u, v): d['weight'] for u, v, d in self.graph.edges(data=True)}

        nx.draw(self.graph, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold', arrows=True)
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels)

        plt.title("Weighted Graph Visualization")
        if not plt.isinteractive():
            plt.show()

# Driver code

test_graph = [[1], [0, 2, 4], [1, 3], [2], [1]]
W = {
    (0, 1): random.randint(-3,3),
    (1, 0): random.randint(-3,3),
    (1, 2): random.randint(-3,3),
    (1, 4): random.randint(-3,3),
    (2, 1): random.randint(-3,3),
    (2, 3): random.randint(-3,3),
    (3, 2): random.randint(-3,3),
    (4, 1): random.randint(-3,3),
}



def bellman_ford(Adj, w, s):
    infinity = float("inf")
    d = [infinity for _ in Adj]
    parent = [None for _ in Adj]
    d[s], parent[s] = 0, s
    V = len(Adj)
    for k in range(V - 1):
        for u in range(V):
            for v in Adj[u]:
                try_to_relax(Adj, w, d, parent, u, v)
    for u in range(V):
        for v in Adj[u]:
            if d[v] > d[u] + w(u, v):
                raise Exception("Ack! There is a negative weight cycle!")

    return d, parent

graph_visualizer = GraphVisualizer(test_graph, W)
graph_visualizer.draw_graph()