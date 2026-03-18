def reorderLogFiles(logs: list[str]) -> list[str]:
    def build_tuple(log):
        if log[0].isdigit():
            return (1,)
        return (0, len(log), log.lower(), sum(c.islower() for c in log))

    return sorted(logs, key=build_tuple)


logs = [
    "Act car",
    "act Car",
    "123 456",
    "Zoo park",
    "apple pie",
    "aaa",
    "Aaa",
    "AAA",
    "bbb",
    "BBB",
]

print(reorderLogFiles(logs))
