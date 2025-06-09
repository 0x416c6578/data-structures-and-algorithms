"""
An adjacency list implementation of a directed acyclic graph
"""
from asyncio import get_child_watcher


class DAG:
    def __init__(self):
        # The graph is represented as a dictionary mapping Node -> [Node] from a node to it's children
        self.graph = {}

    def get_graph(self):
        return self.graph.copy()

    def add_node(self, new_node):
        """
        Add a new node to the graph
        :param new_node: Node to add
        :return: None
        """
        self.graph.setdefault(new_node, set())  # Add the new node, making sure not to overwrite

    def add_edge(self, source_node, destination_node):
        if self._creates_cycle(source_node, destination_node):
            raise ValueError("Adding this edge would create a cycle")
        self.graph[source_node].add(destination_node)

    def get_children(self, node) -> list:
        """
        Depth first recursive to retrieve children
        :param node: Node to find the children of
        :return: Set containing all it's children
        """
        if self.graph.get(node) is None:
            return []

        children = set()
        for child in self.graph[node]:
            children = children.union(child).union(self.get_children(child))
        return children

    def has_child(self, node, target):
        """
        Determine whether a node has a specified child
        :param node: The node to check
        :param target: The child to search for
        :return:
        """
        return target in self.get_children(node)

    def _creates_cycle(self, source_node, destination_node):
        """
        DFS to detect a cycle from the destination node to see if it loops back to the source node - if so, adding that new
        edge would create a cycle which breaks the DAG invariant so the edge can't be added
        :param source_node: The source node of the edge
        :param destination_node: The destination node of the edge
        :return:
        """
        visited = []
        to_visit = [destination_node]

        while to_visit:
            # Grab the next node to visit in the stack
            next_node = to_visit.pop()
            # Add it to the list of visited nodes
            visited.append(next_node)
            # Add its children to the stack of nodes to visit next
            to_visit = to_visit + list(self.graph[next_node])

            if source_node in visited:
                # We have hit the source node - adding this new edge would create a cycle which we don't want
                return True

        return False