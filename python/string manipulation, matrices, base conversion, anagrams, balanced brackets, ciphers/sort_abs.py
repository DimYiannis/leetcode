def sort_by_abs(arr: list[list[int]]) -> list[list[int]]:
    return [sorted(sub, key=abs) for sub in arr]

# or

def sort_by_abs(arr):
    for sub in arr:
        sub.sort(key=abs)
    return arr
