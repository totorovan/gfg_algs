from linkedlist_algs.node import Node


def reverse_list(head: Node):
    prev_node = None
    current_node = head
    while current_node is not None:
        next_node = current_node.next
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node
    return prev_node
