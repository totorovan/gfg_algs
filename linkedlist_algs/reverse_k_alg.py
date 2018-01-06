from linkedlist_algs.node import Node


def reverse(head: Node, k):
    if head is None or k == 1:
        return head

    current_node = head
    current_last = head
    prev_last = None
    new_head = None
    while current_node is not None:
        next_node = current_node.next
        current_last = current_node
        i = 0
        while i < k - 1 and next_node is not None:
            tmp = next_node.next
            next_node.next = current_node
            current_node = next_node
            next_node = tmp
            i += 1
        if prev_last is not None:
            prev_last.next = current_node
        else:
            new_head = current_node
        prev_last = current_last
        current_node = next_node
    current_last.next = None
    return new_head
