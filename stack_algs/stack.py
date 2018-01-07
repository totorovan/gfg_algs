def is_empty(stack):
    return len(stack) == 0


def push(stack, x):
    stack.append(x)


def raise_on_empty(stack):
    if is_empty(stack):
        raise Exception("Empty stack")


def pop(stack):
    raise_on_empty(stack)
    return stack.pop()


def peek(stack):
    raise_on_empty(stack)
    return stack[-1]