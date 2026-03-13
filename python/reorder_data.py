def reorderLogFiles(logs:list[str]) -> list[str]:
    def build_tuple(log):
        if log[0].isdigit():
            return (1,)
        return (0, log)
    return sorted(logs, key=build_tuple)





logs = [
    "dog bark",
    "cat meow",
    "apple pie",
    "zebra run",
    "123 456",
    "7 8 9",
    "banana split",
    "alpha beta"
]

print(reorderLogFiles(logs))
