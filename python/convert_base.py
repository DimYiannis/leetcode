"""
write a function that converts a number from one base to another.
support bases from 2 to 36 inclusive using digits 0-9 and letters A-Z
for values 10-35. return error for invalid inputs (base, digits)
"""

import string

DIGITS = string.digits + string.ascii_uppercase


def convert_base(num_str: str, from_base: int, to_base: int) -> str:

    if not (2 <= from_base <= 36 and 2 <= to_base <= 36):
        return "ERROR"

    try:
        value = int(num_str, from_base)
    except Exception:
        return "ERROR"

    if value == 0:
        return "0"
    result = []
    while value > 0:
        value, remainder = divmod(value, to_base)
        result.append(DIGITS[remainder])

    result = "".join(reversed(result))
    return result


print(convert_base("255", 10, 16))
print(convert_base("13", 10, 2))  # 1101
print(convert_base("42", 10, 8))  # 52
print(convert_base("100", 10, 16))  # 64

print(convert_base("123", 10, 7))  # 234
print(convert_base("255", 10, 2))  # 11111111
print(convert_base("512", 10, 8))  # 1000

print(convert_base("26", 10, 16))  # 1A
print(convert_base("31", 10, 16))  # 1F
print(convert_base("1000", 10, 16))  # 3E8

print(convert_base("1011", 2, 10))  # 11
print(convert_base("77", 8, 10))  # 63
print(convert_base("1A", 16, 10))  # 26

print(convert_base("101101", 2, 16))  # 2D
print(convert_base("7B", 16, 2))  # 1111011
print(convert_base("345", 6, 10))  # 137

print(convert_base("0", 10, 2))  # 0
print(convert_base("1", 10, 2))  # 1
print(convert_base("ZZ", 36, 10))  # 1295

print(convert_base("1234", 10, 5))  # 14414
print(convert_base("ABC", 16, 10))  # 2748
