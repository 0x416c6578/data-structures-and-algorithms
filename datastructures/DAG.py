"""
An adjacency list implementation of a directed acyclic graph
"""
class DAG:
    def __init__(self):
        # The graph is represented as a dictionary mapping Node -> [Node] from a node to it's children
        self.graph = {}

    def add_node(self, new_node):
        """
        Add a new node to the graph
        :param new_node: Node to add
        :return: None
        """
        self.graph.setdefault(new_node, set()) # Add the new node, making sure not to overwrite

    def add_edge(self, from_node, to_node):
        if self._creates_cycle(from_node, to_node):
            raise ValueError("Adding this edge would create a cycle")

    def _creates_cycle(self, from_node, to_node):
        """
        DFS to detect a cycle
        :param from_node:
        :param to_node:
        :return:
        """
        # TODO: Finish implementation