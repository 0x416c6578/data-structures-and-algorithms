from algorithms.BinarySearch import binary_search
from algorithms.Search import breadth_first
from algorithms.SelectionSort.SelectionSort import selection_sort_recursive
from algorithms.IntervalMerge.IntervalMerge import merge_intervals
from datastructures import DAG

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

    print(merge_intervals([(0,1),(3,6),(2,4),(9,12)]))

    dag = DAG.DAG()
    dag.add_node("A")
    dag.add_node("B")
    dag.add_node("C")
    print(dag.get_graph())
    dag.add_edge("A", "B")
    dag.add_edge("A", "C")
    dag.add_edge("B", "C")
    print(dag.get_graph())
    try:
        dag.add_edge("B", "A")
    except ValueError as e:
        print(e)
    print(dag.get_children("A"))