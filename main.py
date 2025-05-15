from algorithms.BinarySearch import binary_search
from algorithms.Search import breadth_first
from algorithms.SelectionSort import selection_sort_recursive

if __name__ == '__main__':
    print(binary_search([1, 2, 3, 7, 8, 11, 15, 21], 11))
    print(selection_sort_recursive([1, 5, 20, 6, 5, 1]))

    adjacency_graph = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["D", "E"],
        "D": [],
        "E": ["F"],
        "F": ["D", "G"]
    }

    breadth_first(adjacency_graph, "G")
    breadth_first(adjacency_graph, "G")
