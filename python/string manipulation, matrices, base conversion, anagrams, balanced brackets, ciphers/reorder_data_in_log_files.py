def parsed_string(s: str) -> str:
    # s = "dig1 1 2 3"
    listt = s.split(" ", 1)
    # list = ["dig1" "1 2 3"]
    string = listt[1]
    return string
    # return "1 2 3"


def is_letters(s: str) -> bool:
    string = parsed_string(s)
    string_without_spaces = string.replace(" ", "")
    return string_without_spaces.isalpha()


def reorderLogFiles(logs: list[str]) -> list[str]:
    length = len(logs)
    for i in range(length - 1):

        for j in range(0, length - i - 1):
            # letters first
            if is_letters(logs[j]) == False and is_letters(logs[j + 1]):
                logs[j], logs[j + 1] = logs[j + 1], logs[j]

            # lexicographically order in only-letters strings
            elif is_letters(logs[j]) and is_letters(logs[j + 1]):
                if parsed_string(logs[j]) > parsed_string(logs[j + 1]):
                    logs[j], logs[j + 1] = logs[j + 1], logs[j]

                # compare the identifiers
                elif parsed_string(logs[j]) == parsed_string(logs[j + 1]):
                    if logs[j].split()[0] > logs[j + 1].split()[0]:
                        logs[j], logs[j + 1] = logs[j + 1], logs[j]
    return logs


def reorderLogFiles(logs: list[str]) -> list[str]:
    def key(log):
        id_, rest = log.split(" ", 1)
        if rest[0].isdigit():
            return (1,)
        return (0, rest, id_)

    return sorted(logs, key=key)


logs1 = [
    "dig1 8 1 5 1",
    "let1 art can",
    "dig2 3 6",
    "let2 own kit dig",
    "let3 art zero",
]
logs2 = [
    "a1 9 2 3 1",
    "g1 act car",
    "zo4 4 7",
    "ab1 off key dog",
    "a8 act zoo",
    "a2 act car",
]
logs3 = ["j mo", "5 m w", "t q h", "g 07", "o 2 0"]
logs4 = [
    "a1 9 2 3 1",
    "g1 act car",
    "zo4 4 7",
    "ab1 off key dog",
    "a8 act zoo",
    "a2 act car",
]
logs5 = ["zoey i love you", "lucas i love you", "rong i love you"]
logs6 = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]
print(reorderLogFiles(logs6))
