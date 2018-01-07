from stack_algs.stack import is_empty, push, pop, peek


def ngl(ar):
    if len(ar) == 0:
        return

    stack = []
    push(stack, ar[0])
    for i in range(1, len(ar)):
        if not is_empty(stack):
            while not is_empty(stack) and peek(stack) < ar[i]:
                print(str(pop(stack)) + " - " + str(ar[i]))
        push(stack, ar[i])

    while not is_empty(stack):
        print(str(pop(stack)) + " - " + str(-1))


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        arr = []
        input()
        arr = [int(n) for n in input().split()]
        ngl(arr)
        print()
