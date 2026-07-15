"""
→ count consecutive number pairs in string,
 second digit is 1 greater than last (0–9)
 → str as input
"""


def count_consecutive_pairs(s: str) -> int:
    count = 0
    for i in range(len(s) - 1):
        if int(s[i]) == int(s[i + 1]) - 1:
            count += 1
    return count


print(count_consecutive_pairs("12345123"))
