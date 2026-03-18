def rotate_right(arr: list, k: int) -> list:
    if not arr:
        return arr

    k = k % len(arr)  # handle k > n
    return arr[-k:] + arr[:-k]