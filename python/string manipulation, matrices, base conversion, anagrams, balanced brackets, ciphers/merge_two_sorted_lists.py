def mergeTwoLists(list1: list, list2: list) -> list:
    result = []
    result = list(list1)
    result += list(list2)
    result = sorted(result)
    return result




print(mergeTwoLists([], [1,2]))
print(mergeTwoLists([1,2], []))
print(mergeTwoLists([1,1,1], [1,1]))


