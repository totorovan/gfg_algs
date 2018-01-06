from linkedlist_algs.node import Node


def rotate_list(head: Node, k):
    new_head = head
    for i in range(k):
        new_head = new_head.next
    last = new_head
    while last.next is not None:
        last = last.next
    current = head
    for j in range(k):
        last.next = current
        current = current.next
        last = last.next
    last.next = None

    return new_head
