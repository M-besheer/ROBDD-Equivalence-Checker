import networkx as nx
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
from collections import defaultdict


def plot_robdd(input_nodes,figname):
    """
    Plot a Reduced Ordered Binary Decision Diagram (ROBDD) with the root node centered.

    Args:
        input_nodes (list): List of nodes where each node is defined as
                            [name, parent, left_child, right_child].
    """

    # Parse input into nodes and edges
    nodes = {}
    edges = []
    edge_labels = {}  # To store labels for edges
    variables = []  # To track unique variables (e.g., 'a', 'b', 'c')
    if input_nodes[0][0] == '/':
        input_nodes.remove(input_nodes[0])
    for i, entry in enumerate(input_nodes):
        node_index = i + 1
        name, parent, left_child, right_child = entry
        nodes[node_index] = {'name': name, 'parent': parent, 'left': left_child, 'right': right_child}

        # Add variables to the list if they're not terminal nodes
        if name.isalpha() and name not in variables:
            variables.append(name)

    # Filter valid nodes and include the first node (index 1) even if its parent is '/'
    valid_nodes = set(idx for idx, node in nodes.items() if node['parent'] != '/' or idx == 1)

    for idx, node in nodes.items():
        parent = node['parent']
        left_child = node['left']
        right_child = node['right']

        # Skip nodes with invalid parents, except the first node (index 1)
        if idx not in valid_nodes:
            continue

        # Correct edges for valid parent-child relationships
        if left_child != '/' and int(left_child) in valid_nodes:
            edges.append((node['name'] + f"_{idx}", nodes[int(left_child)]['name'] + f"_{left_child}"))
            edge_labels[(node['name'] + f"_{idx}", nodes[int(left_child)]['name'] + f"_{left_child}")] = '0'  # Label left edge as '0'
        if right_child != '/' and int(right_child) in valid_nodes:
            edges.append((node['name'] + f"_{idx}", nodes[int(right_child)]['name'] + f"_{right_child}"))
            edge_labels[(node['name'] + f"_{idx}", nodes[int(right_child)]['name'] + f"_{right_child}")] = '1'  # Label right edge as '1'

    # Assign levels to variables
    level_map = {var: i for i, var in enumerate(variables)}
    max_level = len(variables)  # Max level for terminal nodes like 0 and 1

    # Determine total width needed for the bottom level of the pyramid
    total_width = 2 ** max_level - 1

    # Generate positions for nodes in pyramid layout
    pos = {}
    level_counts = defaultdict(int)  # To track the number of nodes at each level

    for idx, node in nodes.items():
        if idx in valid_nodes:
            name = node['name']
            # Determine the level
            if name.isalpha():  # Variables like 'a', 'b', 'c'
                level = level_map[name]
            else:  # Terminal nodes (e.g., '0', '1')
                level = max_level

            # Calculate x and y coordinates for the pyramid structure
            level_width = 2 ** level
            x_spacing = total_width / level_width
            x_pos = (level_counts[level] + 0.5) * x_spacing - total_width / 2  # Center nodes at each level
            y_pos = -level  # Y decreases as level increases
            pos[name + f"_{idx}"] = (x_pos, y_pos)
            level_counts[level] += 1

    # Center the root node (level 0) exactly at the middle of the x-axis
    root_name = nodes[1]['name'] + "_1"  # Root node is always index 1
    root_x, root_y = pos[root_name]
    offset = total_width / 2 - root_x
    for node_name in pos:
        x, y = pos[node_name]
        pos[node_name] = (x + offset, y)

    # Create the directed graph
    G = nx.DiGraph()
    for edge in edges:
        G.add_edge(*edge)

    # Plot the graph with differentiated edges
    plt.figure(figsize=(8, 6))
    edge_colors = [
        'blue' if edge_labels[edge] == '0' else 'red'
        for edge in G.edges
    ]  # '0' edges are blue, '1' edges are red
    nx.draw(
        G, pos, with_labels=True, node_size=2000, node_color="skyblue",
        font_size=10, arrowsize=20, edge_color=edge_colors, width=2
    )

    # Add labels to edges for '0' and '1'
    nx.draw_networkx_edge_labels(
        G, pos, edge_labels=edge_labels, font_size=10, font_color="black"
    )

    plt.title("Centered Pyramid-Structured Reduced Ordered Binary Decision Diagram (ROBDD)")
    plt.gcf().canvas.manager.set_window_title(figname)
    plt.show()



"""
# Example Input
input_nodes = [
    ['a', '/', '4', '3'],  # First node (index 1) has parent '/', but it should still appear
    ['b', '/', '4', '4'],  # This node should not appear
    ['b', '1', '4', '9'],  # Valid node with parent '1'
    ['c', '1', '8', '9'],  # Valid node with parent '1'
    ['c', '/', '8', '9'],  # This node should not appear
    ['c', '/', '8', '9'],  # This node should not appear
    ['c', '/', '9', '9'],  # This node should not appear
    ['0', '4', '/', '/'],  # Valid terminal node
    ['1', '3', '/', '/'],  # Valid terminal node
    ['0', '/', '/', '/'],  # Valid terminal node
    ['1', '/', '/', '/'],  # Valid terminal node
    ['0', '/', '/', '/'],  # Valid terminal node
    ['1', '/', '/', '/'],  # Valid terminal node
    ['0', '/', '/', '/'],  # Valid terminal node
    ['1', '/', '/', '/'],  # Valid terminal node
]

# Plot the ROBDD
plot_robdd(input_nodes)


input_nodes = [
     ['a', '/', '2', '3'],
     ['b', '1', '4', '5'],
     ['b', '1', '6', '7'],
     ['c', '2', '8', '9'],
     ['c', '2', '10', '11'],
     ['c', '3', '12', '13'],
     ['c', '3', '14', '15'],
     ['0', '4', '/', '/'],
     ['1', '4', '/', '/'],
     ['0', '5', '/', '/'],
     ['1', '5', '/', '/'],
     ['0', '6', '/', '/'],
     ['1', '6', '/', '/'],
     ['1', '7', '/', '/'],
     ['1', '7', '/', '/'],
 ]
plot_robdd(input_nodes)
"""

# input_nodes = [
#     ['a', '/', '4', '3'],  # First node (index 1) has parent '/', but it should still appear
#     ['b', '/', '4', '4'],  # This node should not appear
#     ['b', '1', '4', '9'],  # Valid node with parent '1'
#     ['c', '1', '8', '9'],  # Valid node with parent '1'
#     ['c', '/', '8', '9'],  # This node should not appear
#     ['c', '/', '8', '9'],  # This node should not appear
#     ['c', '/', '9', '9'],  # This node should not appear
#     ['0', '4', '/', '/'],  # Valid terminal node
#     ['1', '3', '/', '/'],  # Valid terminal node
#     ['0', '/', '/', '/'],  # Valid terminal node
#     ['1', '/', '/', '/'],  # Valid terminal node
#     ['0', '/', '/', '/'],  # Valid terminal node
#     ['1', '/', '/', '/'],  # Valid terminal node
#     ['0', '/', '/', '/'],  # Valid terminal node
#     ['1', '/', '/', '/'],  # Valid terminal node
# ]