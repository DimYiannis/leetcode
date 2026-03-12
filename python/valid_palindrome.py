
def isPalindrome(s: str) -> bool:
    s = s.lower()
    # print(s)

    clean_s = ''.join(filter(str.isalnum, s))
    # print(clean_s)
    return clean_s == clean_s[::-1]


print(isPalindrome("A man, a plan, a canal: Panama"))
