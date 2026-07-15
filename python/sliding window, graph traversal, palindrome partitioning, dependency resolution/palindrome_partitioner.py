# Assignment name  : py_palindrome_partitioner
# Expected files   : py_palindrome_partitioner.py
# Allowed functions: None
# --------------------------------------------------------------------------------

# Write a function that finds the minimum number of cuts needed to partition a string so that every substring is a palindrome.

# Your function must be declared as follows:

# def palindrome_partitioner(s: str) -> int:

# The function should:
# - Find minimum cuts to make all parts palindromes
# - Return the number of cuts needed (not the number of parts)
# - Handle empty strings (return 0)
# - Single characters are palindromes
# - Case-sensitive palindrome checking

# Examples:

# Input: palindrome_partitioner("aab")
# Output: 1
# # Cut: "a|ab" -> "a" and "ab" (but "ab" is not palindrome)
# # Cut: "aa|b" -> "aa" and "b" (both palindromes) - 1 cut

# Input: palindrome_partitioner("aba")
# Output: 0
# # "aba" is already a palindrome - 0 cuts

# Input: palindrome_partitioner("abcba")
# Output: 0
# # "abcba" is already a palindrome - 0 cuts

# Input: palindrome_partitioner("abcd")
# Output: 3
# # "a|b|c|d" -> 3 cuts needed

# Input: palindrome_partitioner("aabaa")
# Output: 0
# # "aabaa" is already a palindrome - 0 cuts needed

# Input: palindrome_partitioner("abac")
# Output: 1
# # "aba|c" -> 1 cut needed ("aba" and "c" are palindromes)

# Input: palindrome_partitioner("")
# Output: 0

def palindrome_partitioner(s: str) -> int:
    if not s:
        return 0
    n = len(s)
    dp = list(range(n))
    for i in range(n):
        for j in range(i + 1):
            if s[j:i+1] == s[j:i+1][::-1]:
                dp[i] = 0 if j == 0 else min(dp[i], dp[j-1] + 1)
    return dp[-1]


# res = palindrome_partitioner("aab")
# print(f"excepted: 1")
# print(f"got: {res}\n")

# res = palindrome_partitioner("aba")
# print(f"excepted: 0")
# print(f"got: {res}\n")

# res = palindrome_partitioner("abcba")
# print(f"excepted: 0")
# print(f"got: {res}\n")

# res = palindrome_partitioner("abcd")
# print(f"excepted: 3")
# print(f"got: {res}\n")

# res = palindrome_partitioner("aabaa")
# print(f"excepted: 0")
# print(f"got: {res}\n")

# res = palindrome_partitioner("abac")
# print(f"excepted: 1")
# print(f"got: {res}\n")

# res = palindrome_partitioner("")
# print(f"excepted: 0")
# print(f"got: {res}\n")