import networkx as nx
import matplotlib.pyplot as plt

# Define the graph
G = nx.DiGraph()

# Add nodes with positions (for visualization)
positions = {
    'L_G': (0, 0),
    'L_A': (1, 1),
    'L_B': (1, -1),
    'L_C': (2, 2),
    'L_D': (2, 0),
    'L_E': (2, -2)
}

G.add_node('L_G', pos=positions['L_G'])
G.add_node('L_A', pos=positions['L_A'])
G.add_node('L_B', pos=positions['L_B'])
G.add_node('L_C', pos=positions['L_C'])
G.add_node('L_D', pos=positions['L_D'])
G.add_node('L_E', pos=positions['L_E'])

# Add edges with weights
edges = [
    ('L_G', 'L_A', 5),
    ('L_G', 'L_B', 3),
    ('L_A', 'L_C', 4),
    ('L_B', 'L_D', 2),
    ('L_C', 'L_D', 6),
    ('L_B', 'L_E', 7)
]

G.add_weighted_edges_from(edges)

# Get positions
pos = nx.get_node_attributes(G, 'pos')

# Draw the graph
plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, font_weight='bold', arrows=True)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title('Graph Visualization of Landmarks and Trails')
plt.show()
