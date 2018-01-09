class Stack:
    s = []

    def __init__(self):
        self.min = None

    def is_empty(self):
        return self.s == []

    def get_min(self):
        if self.is_empty():
            raise Exception("Empty stack")
        return self.min

    def push(self, x):
        if self.is_empty():
            self.min = x
            self.s.append(x)
            return
        if x >= self.min:
            self.s.append(x)
        else:
            self.s.append(2 * x - self.min)
            self.min = x

    def pop(self):
        if self.is_empty():
            raise Exception("Empty stack")
        x = self.s.pop()
        if x >= self.min:
            return x
        tmp = self.min
        self.min = 2 * self.min - x
        return tmp


if __name__ == '__main__':
    s = Stack()
    s.push(3)
    s.push(2)
    s.push(4)
    print(s.get_min())
    print(s.pop())
    print(s.get_min())
    print(s.pop())
    print(s.get_min())