from linkedlist_algs.node import Node
from linkedlist_algs.reverse_k_alg import reverse


def print_list(head):
    current = head
    while current is not None:
        print(current)
        current = current.next


if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node8 = Node(8)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = node8
    print_list(reverse(node1, 4))
