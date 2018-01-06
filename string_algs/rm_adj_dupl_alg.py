def remove_adjacent_duplicates(s):
    n = len(s)
    i = 1
    res = ""
    while i < n:
        if s[i - 1] != s[i]:
            res += s[i - 1]
        else:
            while i < n and s[i - 1] == s[i]:
                i += 1
        i += 1

    if i == n:
        res += s[i - 1]

    if len(res) == n:
        return res

    return remove_adjacent_duplicates(res)
