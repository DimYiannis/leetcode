def isValid(s: str) -> bool:
    if len(s) % 2 != 0:
        return False
    else:
        stack = []
        i = 0
        while i < len(s):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                stack.append(s[i])
                i += 1
            else:
                if len(stack) == 0:
                    return False
                elif s[i] == ")" and stack.pop() == "(":
                    i += 1
                elif s[i] == "}" and stack.pop() == "{":
                    i += 1 
                elif s[i] == "]" and stack.pop() == "[":
                    i += 1
                else:
                    return False
        return len(stack) == 0


if __name__ == "__main__":
    case_1 = "()"
    case_2 = "(([]))[]{}"
    case_3 = "(]"
    case_4 = "([])"
    case_5 = "([)]"
    case_6 = "fgs(grgs)sgfsa(sagsa)"
    case_7 = ")("


print(isValid(case_6))
