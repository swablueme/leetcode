
# %%
import networkx as nx
from networkx import Graph
from trie import Trie


def draw_trie(trie: Trie) -> None:
    G = nx.Graph()
    bfs_trie(trie, G, None)
    labels = nx.get_node_attributes(G, 'value')
    nx.draw_networkx(G, with_labels=True,
                     labels=labels)


def bfs_trie(object: Trie, graph: Graph, previous=None):
    if hasattr(object, "node"):
        bfs_trie(getattr(object, "node"), graph, previous)
    if hasattr(object, "children"):
        for _, value in getattr(object, "children").items():
            graph.add_node(value, **value.__dict__)
            if previous is not None:
                graph.add_edge(object, value)
            bfs_trie(value, graph, object)


hello = Trie()
hello.insert("asdfsf")
draw_trie(hello)

# %%
