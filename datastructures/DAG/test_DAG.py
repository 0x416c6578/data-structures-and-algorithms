from unittest import TestCase
from DAG import DAG


class TestDAG(TestCase):
    def setUp(self):
        self.graph = DAG()

    def test_get_graph(self):
        # Retrieve graph representation
        self.assertEqual(self.graph.get_graph(), {})
        self.graph.add_node("A")
        self.assertEqual(self.graph.get_graph(), {"A": set()})
        self.graph.add_node("B")
        self.assertEqual(self.graph.get_graph(), {"A": set(), "B": set()})
        self.graph.add_edge("A", "B")
        self.assertEqual(self.graph.get_graph(), {"A": {"B"}, "B": set()})

    def test_add_node(self):
        self.graph.add_node("A")
        self.assertEqual(self.graph.get_graph(), {"A": set()})
        self.graph.add_node("A")
        self.assertEqual(self.graph.get_graph(), {"A": set()})
        self.graph.add_node("B")
        self.assertEqual(self.graph.get_graph(), {"A": set(), "B": set()})

    def test_remove_node(self):
        self.graph.add_node("A")
        self.graph.add_node("B")
        self.graph.add_edge("A", "B")
        self.assertEqual(self.graph.get_graph(), {"A": {"B"}, "B": set()})
        self.graph.remove_node("B")
        self.assertEqual(self.graph.get_graph(), {"A": set()})
        self.graph.remove_node("B")
        self.assertEqual(self.graph.get_graph(), {"A": set()})
        self.graph.remove_node("A")
        self.assertEqual(self.graph.get_graph(), {})

    def test_add_edge(self):
        self.graph.add_node("A")
        # Adding an edge with invalid source or destination
        with self.assertRaises(ValueError):
            self.graph.add_edge("A", "C")
        with self.assertRaises(ValueError):
            self.graph.add_edge("C", "A")
        self.assertEqual(self.graph.get_graph(), {"A": set()})

        # Add a valid edge
        self.graph.add_node("B")
        self.graph.add_edge("A", "B")
        self.assertEqual(self.graph.get_graph(), {"A": {"B"}, "B": set()})
        self.graph.add_edge("A", "B")
        self.assertEqual(self.graph.get_graph(), {"A": {"B"}, "B": set()})

        # Add a direct loop
        with self.assertRaises(ValueError):
            self.graph.add_edge("B", "A")



    def test_add_edge_cycles_detection(self):
        pass

    def test_get_children(self):
        pass

    def test_has_child(self):
        pass

    def test__creates_cycle(self):
        pass
