import unittest
from cost_calculator import calculate_graph_cost, calculate_distance, get_cabinet_node_id
import networkx as nx


class TestCostCalculator(unittest.TestCase):
    def setUp(self):
        # reading the given file for test cases.
        self.graph = nx.read_graphml('test.graphml')

    def test_get_cabinet_node_id(self):
        self.assertEqual(get_cabinet_node_id(self.graph), 'A')

    def test_calculate_distance(self):
        distance_AF = calculate_distance(self.graph, 'A', 'F')
        self.assertEqual(distance_AF, 50)
        distance_AD = calculate_distance(self.graph, 'A', 'D')
        self.assertEqual(distance_AD, 350)
        distance_AB = calculate_distance(self.graph, 'A', 'B')
        self.assertEqual(distance_AB, 70)
        distance_CA = calculate_distance(self.graph, 'C', 'A')
        self.assertEqual(distance_CA, 200)

    def test_calculate_graph_cost_A(self):
        rate_card_A = {'Cabinet': 1000, 'Chamber': 200, 'road': 100, 'verge': 50, 'Pot': 100}
        cost_A = calculate_graph_cost(self.graph, rate_card_A, pot_price_fixed=True)
        self.assertEqual(cost_A, 42200)

    def test_calculate_graph_cost_B(self):
        rate_card_B = {'Cabinet': 1200, 'Chamber': 200, 'road': 80, 'verge': 40, 'Pot': 20}
        cost_B = calculate_graph_cost(self.graph, rate_card_B, pot_price_fixed=False)
        self.assertEqual(cost_B, 52400)


if __name__ == '__main__':
    unittest.main()
