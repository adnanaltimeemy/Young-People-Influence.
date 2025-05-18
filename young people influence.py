import random
import networkx as nx
import matplotlib.pyplot as plt

# Create a social network graph
G = nx.erdos_renyi_graph(n=30, p=0.1)

# Randomly assign users as young or not
for node in G.nodes():
    G.nodes[node]['age'] = random.choice(['young', 'older'])
    G.nodes[node]['trend'] = False

# Seed trend with 3 random young users
young_users = [n for n in G.nodes if G.nodes[n]['age'] == 'young']
initial_influencers = random.sample(young_users, 3)

for node in initial_influencers:
    G.nodes[node]['trend'] = True

# Simulate influence spread
def spread_trend(graph, steps=5):
    for step in range(steps):
        new_trending = []
        for node in graph.nodes:
            if not graph.nodes[node]['trend']:
                neighbors = list(graph.neighbors(node))
                trending_neighbors = [n for n in neighbors if graph.nodes[n]['trend']]
                if len(trending_neighbors) >= 2:
                    new_trending.append(node)
        for node in new_trending:
            graph.nodes[node]['trend'] = True

spread_trend(G)

# Visualize results
color_map = []
for node in G.nodes:
    if G.nodes[node]['trend']:
        color_map.append('green')
    elif G.nodes[node]['age'] == 'young':
        color_map.append('blue')
    else:
        color_map.append('gray')

plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_color=color_map, node_size=500)
plt.title("Social Media Trend Spread by Young Influencers")
plt.show()
