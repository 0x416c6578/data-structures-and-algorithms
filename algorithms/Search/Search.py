from collections import deque

def breadth_first(graph : dict, target : str, start : str = "A"):
    """
    Simple breadth first search on an adjacency list structure
    :param graph: The graph to search
    :param target: The target to search for
    :param start: The starting node (defaults to "A")
    :return: Nothing - will print the status as part of this method
    """
    # Set of visited nodes
    visited = set()
    # The bfs queue
    visit_queue = deque()

    # We need somewhere to start
    visit_queue.append(start)

    # Loop while the queue has elements
    while len(visit_queue) != 0:
        # Dequeue next node
        node = visit_queue.popleft()

        if node not in visited:
            # Check for target in the current node
            if node == target:
                print(f"Found target {target} after visiting {visited}")
                return

            # Add this node to the visited set
            visited.add(node)

            # Add unseen neighbours to the queue
            for neighbour in graph.get(node, []):
                if neighbour not in visited:
                    visit_queue.append(neighbour)
    print(f"Couldn't find target {target}")