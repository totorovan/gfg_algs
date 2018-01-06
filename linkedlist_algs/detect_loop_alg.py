from linkedlist_algs.node import Node


def detect_loop(head):
    if head is None or head.next is None:
        return False

    slow = head.next
    fast = head.next.next
    while slow is not None and fast is not None:
        if slow is fast:
            return True
        slow = slow.next
        if fast.next is None:
            return False
        fast = fast.next.next

    return False


if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)

    node1.next = node2
    node2.next = node3
    print(detect_loop(node1))

    node4.next = node5
    node5.next = node6
    node6.next = node4
    print(detect_loop(node4))
