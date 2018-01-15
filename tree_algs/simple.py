def height(root):
    return 0 if root is None else max(root.left, root.right) + 1


def is_leaf(node):
    return node.left is None and node.right is None


def count_leaves(root):
    if root is None:
        return 0
    return 1 if is_leaf(root) else count_leaves(root.left) + count_leaves(root.right)


def find_max_sum_util(root):
    if root is None:
        return 0

    l_max = find_max_sum(root.left)
    r_max = find_max_sum(root.max)

    max_single = max(max(l_max, r_max) + root.data, root.data)

    max_top = max(max_single, l_max + r_max + root.data)
    find_max_sum_util.res = max(find_max_sum_util.res, max_top)

    return max_single


def find_max_sum(root):
    find_max_sum.res = float("-inf")

    find_max_sum_util(root)

    return find_max_sum.res
