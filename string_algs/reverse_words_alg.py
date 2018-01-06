def reverse_words(s, delim='.'):
    n = len(s)
    i = 0
    j = 1
    reversed_words = ""
    while j < n:
        if s[j] == delim:
            reversed_words += (reverse_word(s[i:j]) + delim)
            i = j + 1
            j += 2
        else:
            j += 1
    reversed_words += reverse_word(s[i::])

    return reverse_word(reversed_words)


def reverse_word(s):
    return s[::-1]
