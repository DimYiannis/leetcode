# Assignment name  : py_array_rotation_detector
# Expected files   : py_array_rotation_detector.py
# Allowed functions: None
# --------------------------------------------------------------------------------

# Write a function that determines if one array is a rotation of another array.
# A rotation means the array has been shifted circularly left or right.

# Your function must be declared as follows:

# def array_rotation_detector(arr1: list[int], arr2: list[int]) -> bool:

# The function should:
# - Check if arr2 is a rotation of arr1
# - Handle arrays of different lengths (return False)
# - Handle empty arrays (two empty arrays are rotations)
# - A rotation can be 0 positions (same array)
# - Consider both left and right rotations

# Examples:

# Input: array_rotation_detector([1, 2, 3, 4, 5], [3, 4, 5, 1, 2])
# Output: True

# Input: array_rotation_detector([1, 2, 3, 4, 5], [4, 5, 1, 2, 3])
# Output: True

# Input: array_rotation_detector([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
# Output: True

# Input: array_rotation_detector([1, 2, 3, 4, 5], [2, 3, 4, 5, 1])
# Output: True

# Input: array_rotation_detector([1, 2, 3], [1, 3, 2])
# Output: False

# Input: array_rotation_detector([1, 2, 3], [1, 2])
# Output: False

# Input: array_rotation_detector([], [])
# Output: True

# Input: array_rotation_detector([1, 1, 1], [1, 1, 1])
# Output: True


def array_rotation_detector(arr1: list[int], arr2: list[int]) -> bool:
    if len(arr1) != len(arr2):
        return False
    if not arr1:
        return True
    n = len(arr1)
    doubled = arr1 + arr1
    return any(doubled[i:i+n] == arr2 for i in range(n))


# print(array_rotation_detector([1, 2, 3, 4, 5], [3, 4, 5, 1, 2])) #True
# print(array_rotation_detector([1, 2, 3, 4, 5], [4, 5, 1, 2, 3])) #True
# print(array_rotation_detector([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])) #True
# print(array_rotation_detector([1, 2, 3, 4, 5], [2, 3, 4, 5, 1])) #True
# print(array_rotation_detector([1, 2, 3], [1, 3, 2]))             #False
# print(array_rotation_detector([1, 2, 3], [1, 2]))                #False
# print(array_rotation_detector([], []))                            #True
# print(array_rotation_detector([1, 1, 1], [1, 1, 1]))             #True