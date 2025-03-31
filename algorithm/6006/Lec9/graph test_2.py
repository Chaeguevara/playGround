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


G = GraphVisualization()

test_graph = [[1], [0, 2], [1, 3, 4], [2, 5], [2, 5], [3, 4]]
# visualize graph
for i, item in enumerate(test_graph):
    for v in item:
        G.addEdge(i, v)


def bfs(Adj: list[int], s: int) -> list[int | None]:
    parent: list[int:None] = [None for _ in Adj]
    parent[s] = s
    level = [[s]]
    while 0 < len(level[-1]):
        level.append([])
        for u in level[-2]:  # 0
            for v in Adj[u]:  # Adj[0] => 1
                if parent[v] is None:  # parent[1] is None
                    parent[v] = u  # parent[1] -> 0
                    level[-1].append(v)  #
    return parent




def unweighted_shortest_path(Adj: list[int], s: int, t: int) -> list[int | None] | None:
    parent = bfs(Adj, s)
    if parent[t] is None:
        return None
    cur = t
    path=[t]
    while cur!=s:
        cur = parent[cur]
        path.append(cur)

    return path[::-1]

print(f"{bfs(test_graph,0)=}")
print(f"{unweighted_shortest_path(test_graph,0,5)}")

G.visualize()
