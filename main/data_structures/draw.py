
# %%
import networkx as nx

from trie import Trie


def draw_trie(trie: Trie) -> None:
    G = nx.Graph()


def bfs_trie(object, graph, previous=None):
    if hasattr(object, "node"):
        bfs_trie(getattr(object, "node"), graph, previous)
    if hasattr(object, "children"):
        for key, value in getattr(object, "children").items():
            graph.add_node(value, **value.__dict__)
            if previous is not None:
                graph.add_edge(object, value)
                print("adding edge", object, value)
            print(key)
            bfs_trie(value, graph, object)


hello = Trie()
hello.insert("asdfsf")

graph = nx.Graph()
bfs_trie(hello, graph, None)
labels = nx.get_node_attributes(graph, 'value')
nx.draw_networkx(graph, with_labels=True,
                 labels=labels)

# %%
