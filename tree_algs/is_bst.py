import sys

from tree_algs.node import Node

max_int = sys.maxsize
min_int = -max_int - 1


def is_bst_util(node: Node, min_val, max_val):
    if node is None:
        return True
    if node.data < min_val or node.data > max_val:
        return False
    return is_bst_util(node.left, min_val, node.data) and is_bst_util(node.right, node.data, max_val)


def is_bst(root: Node):
    return is_bst_util(root, min_int, max_int)
