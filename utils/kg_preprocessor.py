import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from pathlib import Path

# Load cleaned triples
TRIPLES_CSV = "data/triples_clean.csv"
GRAPH_IMAGE = "kg/graph_clean.png"
GRAPH_GEXF = "kg/graph_clean.gexf"

# Ensure output folders exist
Path("kg").mkdir(parents=True, exist_ok=True)

# Load preprocessed triples
df = pd.read_csv(TRIPLES_CSV)

# Initialize graph
G = nx.DiGraph()
node_type = {}

# Truncate text nodes if needed (already truncated in preprocessing but safe)
def truncate(text, length=60):
    return text if len(text) <= length else text[:length].strip() + "..."

# Add nodes and edges
for _, row in df.iterrows():
    subj = row["Subject"]
    pred = row["Predicate"]
    obj = truncate(row["Object"])

    G.add_node(subj)
    node_type[subj] = "entity"

    G.add_node(obj)
    node_type[obj] = "text"

    G.add_edge(subj, obj, label=pred)

# Assign colors based on node type
node_colors = ["skyblue" if node_type[n] == "entity" else "lightgreen" for n in G.nodes()]

# Draw the graph using shell layout
plt.figure(figsize=(18, 12))
pos = nx.shell_layout(G)

nx.draw(
    G,
    pos,
    with_labels=True,
    node_color=node_colors,
    node_size=2500,
    font_size=9,
    edge_color="gray",
    font_weight="bold"
)

# Draw edge labels
edge_labels = nx.get_edge_attributes(G, "label")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="red", font_size=8)

plt.title("Knowledge Graph from Cleaned MOSDAC Triples", fontsize=14)
plt.tight_layout()
plt.savefig(GRAPH_IMAGE)
plt.show()

# Save graph as GEXF
nx.write_gexf(G, GRAPH_GEXF)
print(f"Graph saved to {GRAPH_GEXF}")
print(f"Graph image saved to {GRAPH_IMAGE}")
