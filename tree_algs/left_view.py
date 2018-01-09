from stack_algs.queue import Queue


class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


def print_left_view(root):
    if root is None:
        return

    q = Queue()
    q.enqueue(root)
    q.enqueue(None)
    print(root.data, end=' ')
    while not q.isEmpty():
        current = q.dequeue()  # type: Node
        if current is not None:
            if current.left is not None:
                q.enqueue(current.left)
            if current.right is not None:
                q.enqueue(current.right)
        else:
            if not q.isEmpty():
                print(q.peek().data, end=' ')
                q.enqueue(None)
