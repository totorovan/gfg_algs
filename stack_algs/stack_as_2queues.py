from stack_algs.queue import Queue


class Stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x):
        self.q1.enqueue(x)

    def pop(self):
        if self.q1.isEmpty():
            raise Exception("Empty stack")
        el = self.q1.dequeue()
        while not self.q1.isEmpty():
            self.q2.enqueue(el)
            el = self.q1.dequeue()
        while not self.q2.isEmpty():
            self.q1.enqueue(self.q2.dequeue())

        return el


if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.pop())
    print(s.pop())
    print(s.pop())
