import networkx as nx
from cost_calculator import calculate_graph_cost


rate_card_A = {'Cabinet': 1000, 'Chamber': 200, 'road': 100, 'verge': 50, 'Pot': 100}
rate_card_B = {'Cabinet': 1200, 'Chamber': 200, 'road': 80, 'verge': 40, 'Pot': 20}


if __name__ == '__main__':
    graph_file = 'problem.graphml'
    graph = nx.read_graphml(graph_file)
    rate_card_A_cost = calculate_graph_cost(graph, rate_card_A)
    rate_card_B_cost = calculate_graph_cost(graph, rate_card_B, pot_price_fixed=False)
    print(f"Rate Card A cost: £{rate_card_A_cost}")
    print(f"Rate Card B cost: £{rate_card_B_cost}")
