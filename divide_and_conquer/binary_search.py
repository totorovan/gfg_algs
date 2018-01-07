def bin_search(arr, lo, hi, key):
    if lo > hi:
        return -1
    mid = lo + ((hi - lo) >> 1)
    if arr[mid] == key:
        return mid
    if arr[mid] > key:
        return bin_search(arr, lo, mid - 1, key)
    return bin_search(arr, mid + 1, hi, key)


if __name__ == '__main__':
    arr = [1, 3, 4, 6, 7]
    print(bin_search(arr, 0, len(arr) - 1, 3))
    print(bin_search(arr, 0, len(arr) - 1, 8))
