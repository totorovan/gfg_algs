from stack_algs.stack import pop, push, is_empty


class Queue:
    s1 = []
    s2 = []

    def is_empty(self):
        return len(self.s1) == 0

    def enqueue(self, x):
        self.s1.append(x)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Empty queue")
        el = pop(self.s1)
        while not self.is_empty():
            push(self.s2, el)
            el = pop(self.s1)
        while not is_empty(self.s2):
            push(self.s1, pop(self.s2))
        return el


if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue())
    q.enqueue(4)
    print(q.dequeue())
