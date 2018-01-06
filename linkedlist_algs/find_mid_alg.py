from linkedlist_algs.node import Node


def find_mid(head: Node):
    fast = head
    slow = head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

    return slow.data
