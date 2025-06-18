"""
An adjacency list implementation of a directed acyclic graph
"""


class DAG:
    def __init__(self):
        # The graph is represented as a dictionary mapping str -> set[str] from a node to it's children
        self.graph: dict[str, set[str]] = {}

    def get_graph(self) -> dict[str, set[str]]:
        """
        Get the current graph
        :return: dict[str, set[str]] representation of the current graph
        """
        return self.graph.copy()

    def add_node(self, new_node: str):
        """
        Add a new node to the graph
        :param new_node: Node to add
        :return: None
        """
        if new_node is None:
            print("New node is None")
            return
        self.graph.setdefault(new_node, set())  # Add the new node, making sure not to overwrite

    def remove_node(self, node_to_remove: str) -> None:
        """
        Remove a node (and it's edges) from the graph
        :param node_to_remove: The node to remove
        :return: None
        """
        if node_to_remove not in self.graph:
            return

        self.graph.pop(node_to_remove)
        for _, connections in self.graph.items():
            if node_to_remove in connections:
                connections.remove(node_to_remove)

    def add_edge(self, source_node: str, destination_node: str) -> None:
        """
        Add an edge to the graph
        :param source_node: The source node of the edge
        :param destination_node: The destination node of the edge
        :return:
        """

        # We could automatically add the missing nodes here, but instead raise a ValueError
        if source_node not in self.graph:
            raise ValueError("Source node not in graph")
        if destination_node not in self.graph:
            raise ValueError("Destination node not in graph")

        if self._creates_cycle(source_node, destination_node):
            raise ValueError("Adding this edge would create a cycle")

        self.graph[source_node].add(destination_node)

    def get_children(self, node) -> set[str]:
        """
        Depth first recursive to retrieve children
        :param node: Node to find the children of
        :return: Set containing all it's children
        """
        if self.graph.get(node) is None:
            return set()

        children = set()
        for child in self.graph[node]:
            children = children.union(child).union(self.get_children(child))
        return children

    def has_child(self, node: str, target: str) -> bool:
        """
        Determine whether a node has a specified child
        :param node: The node to check
        :param target: The child to search for
        :return:
        """
        return target in self.get_children(node)

    def _creates_cycle(self, source_node: str, destination_node: str) -> bool:
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
