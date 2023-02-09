import networkx as nx


def calculate_distance(graph: nx.Graph, start: str, end: str, weight='length') -> float:
    """Calculates shortest distance between two nodes."""
    distance = nx.shortest_path_length(graph, source=start, target=end, weight=weight, method='dijkstra')
    return distance


def get_cabinet_node_id(graph: nx.Graph) -> str:
    """Gets the node ID based on its type."""
    return [node for node, data in graph.nodes.data() if data['type'] == 'Cabinet'][0]


def calculate_graph_cost(graph: nx.Graph, rate_card: dict, pot_price_fixed: bool = True) -> float:
    # calculating cost for nodes
    node_cost = 0
    cabinet_node = get_cabinet_node_id(graph)
    for node, data in graph.nodes.data():
        if data['type'] == 'Pot' and not pot_price_fixed:
            node_cost += calculate_distance(graph, node, cabinet_node) * rate_card['Pot']
        else:
            node_cost += rate_card.get(data['type'], 0)

    # calculating cost for edges
    edge_cost = 0
    for source, targe, data in graph.edges.data():
        edge_cost += rate_card[data['material']] * data['length']

    return node_cost + edge_cost
