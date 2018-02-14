from linkedlist_algs.node import Node


def detect_loop(head):
    if head is None or head.next is None:
        return None

    slow = head.next
    fast = head.next.next
    while slow is not None and fast is not None:
        if slow is fast:
            return slow
        slow = slow.next
        if fast.next is None:
            return None
        fast = fast.next.next

    return None


def detect_and_remove_loop(head):
    mitting_node = detect_loop(head)
    if mitting_node is None:
        return False
    current1 = head
    current2 = mitting_node
    while current1 != current2:
        current1 = current1.next
        current2 = current2.next
    current1.next = None

    return True


if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node1
    print(detect_and_remove_loop(node1))
