import copy
import math
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import itertools
import hashlib
import re


def build_truth_tree(expression, var_order):
    """Builds a binary tree with terminal nodes as results of the expression."""
    num_vars = len(var_order)
    num_rows = 2 ** num_vars
    all_combinations = list(itertools.product([0, 1], repeat=num_vars))

    # Create the terminal leaves from left to right (2^n to 2^(n-1) values)
    terminals = []
    for values in all_combinations:
        var_values = dict(zip(var_order, [bool(val) for val in values]))
        result = evaluate_expression(expression, var_values)
        terminals.append(result)

    return terminals

def printTree(Seifos, n):
    for i in range (0, 2 ** (n+1)):
        print(f"Node number{i}: {Seifos[i]}")


def evaluate_expression(expression, var_values):
    """Evaluates a boolean expression given variable values."""
    expr_with_values = ''.join(
        [str(int(var_values.get(char, False))) if char.isalpha() else char for char in expression])
    expr_with_values = expr_with_values.replace('!', 'not ').replace('&', ' and ').replace('+', ' or ').replace('~',
                                                                                                                'not ').replace(
        '|', ' or ')
    try:
        result = eval(expr_with_values)
        return '1' if result else '0'
    except Exception as e:
        print(f"Error evaluating expression: {e}")
        return None


def getTree(truthTable, n, var_order):
    Seifos = []

    # Add the root node
    Seifos.append(["/", "/", "/", "/"])  # Root (placeholder)
    Seifos.append([var_order[0], "/", "2", "3"])  # First level (root split)

    # Build the tree level by level
    for k in range(1, n):
        start_idx = 2 ** k  # Starting index for level k
        end_idx = 2 ** (k + 1)  # Ending index for level k (exclusive)

        for i in range(start_idx, end_idx):
            parent_idx = i // 2  # Calculate parent index
            left_child_idx = 2 * i
            right_child_idx = 2 * i + 1

            # Append the node for the current level
            Seifos.append([var_order[k], str(parent_idx), str(left_child_idx), str(right_child_idx)])
    start_idx = 2 ** n
    end_idx = 2 ** (n + 1)
    for i in range(start_idx, end_idx):
        parent_idx = i // 2
        Seifos.append([truthTable[i - start_idx], str(parent_idx), '/', '/'])
    print("Bdd:!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    printTree(Seifos, n)
    return Seifos




def doSeifos(BDDSeifos, n,var_order):
    # Step 1: Remove all 0's and 1's and keep only one of each
    zero_count = 0
    zero_index = -1
    one_count = 0
    one_index = -1
    Seifos = copy.deepcopy(BDDSeifos)

    for i in range(2 ** (n - 1), 2 ** n):
        if Seifos[int(Seifos[i][2])][0] == "0":  # Left child
            if zero_count:
                Seifos[int(Seifos[i][2])][1] = "/"
                Seifos[i][2] = str(zero_index)
            else:
                zero_count += 1
                zero_index = int(Seifos[i][2])
        elif Seifos[int(Seifos[i][2])][0] == "1":  # Left child
            if one_count:
                Seifos[int(Seifos[i][2])][1] = "/"
                Seifos[i][2] = str(one_index)
            else:
                one_count += 1
                one_index = int(Seifos[i][2])

        if Seifos[int(Seifos[i][3])][0] == "0":  # Right child
            if zero_count:
                Seifos[int(Seifos[i][3])][1] = "/"
                Seifos[i][3] = str(zero_index)
            else:
                zero_count += 1
                zero_index = int(Seifos[i][3])
        elif Seifos[int(Seifos[i][3])][0] == "1":  # Right child
            if one_count:
                Seifos[int(Seifos[i][3])][1] = "/"
                Seifos[i][3] = str(one_index)
            else:
                one_count += 1
                one_index = int(Seifos[i][3])

    # Step 2: Remove redundant nodes
    for i in range(n, 0, -1):
        for j in range(2 ** (i - 1), 2 ** i):
            if Seifos[j][1] != "/":
                if Seifos[j][2] == Seifos[j][3]:
                    parent = int(Seifos[j][1])
                    if 2 * parent == j:  # Left child
                        Seifos[parent][2] = Seifos[j][2]
                    else:  # Right child
                        Seifos[parent][3] = Seifos[j][2]
                    Seifos[int(Seifos[j][2])][1] = Seifos[j][1]
                    Seifos[j][1] = "/"
                else:
                    for k in range(j + 1, 2 ** i):
                        if Seifos[k][1] != "/" and Seifos[j][2:] == Seifos[k][2:]:
                            parent = int(Seifos[k][1])
                            if 2 * parent == k:  # Left child
                                Seifos[parent][2] = str(j)
                            else:  # Right child
                                Seifos[parent][3] = str(j)
                            Seifos[k][1] = "/"

    # Step 3: Print the optimized BDD
    print("Seifos:!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    for i in range(2 ** (n + 1)):
         print(f"Node number {i} : {Seifos[i]}")

        # Step 3: Sort nodes based on their variables before returning
    valid_nodes = []
    for i in range(len(Seifos)):
        if Seifos[i][1] != "/" or i == 1:
            valid_nodes.append((i, Seifos[i]))

    def sort_key(item):
        index, node_data = item
        if node_data[0] == "/" or node_data[0].isdigit():
            return (len(var_order) + 1, 0)
        else:
            return (var_order.index(node_data[0]), index)

    sorted_nodes = sorted(valid_nodes, key=sort_key)
    sorted_seifos = []
    sorted_seifos.append(copy.deepcopy(Seifos[1]))
    for index, item in sorted_nodes[1:]:
        sorted_seifos.append(copy.deepcopy(item))

    # Step 4: Update indices after sorting
    new_indices = {old_index: new_index for new_index, (old_index, _) in
                   enumerate(sorted_nodes)}  # create a mapping of old indices to new indices

    for i in range(len(sorted_seifos)):
        if sorted_seifos[i][1] != "/" and sorted_seifos[i][1].isdigit():  # update parent
            sorted_seifos[i][1] = str(new_indices[int(sorted_seifos[i][1])])
        if sorted_seifos[i][2] != "/" and sorted_seifos[i][2].isdigit():  # update left child
            sorted_seifos[i][2] = str(new_indices[int(sorted_seifos[i][2])])
        if sorted_seifos[i][3] != "/" and sorted_seifos[i][3].isdigit():  # update right child
            sorted_seifos[i][3] = str(new_indices[int(sorted_seifos[i][3])])

    return Seifos,sorted_seifos


def evaluate_seifos(seifos, assignment, var_order):
    """Evaluates a Seifos ROBDD for a given variable assignment."""
    current_node_index = 0  # Start at the root node (index 1)

    while True:
        current_node = seifos[current_node_index]
        if current_node[0] == '0' or current_node[0] == '1':
            return int(current_node[0])

        variable = current_node[0]
        var_index = var_order.index(variable)

        if assignment[var_index] == 0:

            if not current_node[2].isdigit():  # Terminal node
                return int(current_node[2])
            current_node_index = int(current_node[2])
        else:
            if not current_node[3].isdigit():
                return int(current_node[3])
            current_node_index = int(current_node[3])


def compare_ROBDD(seifos1, var_order1, seifos2, var_order2):
    """Compares two Seifos ROBDDs using truth table comparison."""
    all_variables = sorted(list(set(var_order1 + var_order2)))
    num_variables = len(all_variables)

    for i in range(2 ** num_variables):
        assignment = [(i >> j) & 1 for j in range(num_variables)]
        val1 = evaluate_seifos(seifos1, assignment, var_order1)
        val2 = evaluate_seifos(seifos2, assignment, var_order2)

        if val1 != val2:
            return False
    return True


def detect_variables(expression):
    """Detects variables in a boolean expression string."""
    variables = re.findall(r'[a-zA-Z]+', expression)  # Find all sequences of letters
    return sorted(list(set(variables)))  # Remove duplicates and sort



def Evaluate(expr1,expr2,varOrder1,varOrder2):
    expression1 = expr1
    detected_vars1 = detect_variables(expression1)
    print("Detected variables in Expression 1:", ", ".join(detected_vars1))
    var_order1_str = varOrder1
    var_order1 = [var.strip() for var in var_order1_str.split(',')]


    expression2 = expr2
    detected_vars2 = detect_variables(expression2)
    print("Detected variables in Expression 2:", ", ".join(detected_vars2))
    var_order2_str = varOrder2
    var_order2 = [var.strip() for var in var_order2_str.split(',')]



    # Build the truth tree (BDD)
    Terminals1 = build_truth_tree(expression1, var_order1)
    Terminals2 = build_truth_tree(expression2, var_order2)
    # Print the Binary Decision Diagram (BDD)

    BDDSeifos1 = getTree(Terminals1, len(var_order1), var_order1)
    BDDSeifos2 = getTree(Terminals2, len(var_order2), var_order2)

    ROBDDSeifos1,sortedROBDD1 = doSeifos(BDDSeifos1, len(var_order1),var_order1)  # Simulate Seifos data
    ROBDDSeifos2,sortedROBDD2 = doSeifos(BDDSeifos2, len(var_order2),var_order2)  # Simulate Seifos data

    print("BDD1 output after optimization: ")
    printTree(BDDSeifos1, len(var_order1))

    if compare_ROBDD(sortedROBDD1, var_order1, sortedROBDD2, var_order2):
        print("true")
        return "True" , BDDSeifos1, BDDSeifos2, ROBDDSeifos1, ROBDDSeifos2
    else:
        print("false")
        return "False" , BDDSeifos1, BDDSeifos2, ROBDDSeifos1, ROBDDSeifos2


if __name__ == "__main__":
    expr1 = "A&B&C"
    expr2 = "X&Y&Z"
    varOrder1 = "B,A,C"
    varOrder2 = "X,Y,Z"
    Evaluate(expr1,expr2,varOrder1,varOrder2)
