def whisper_cipher(s: str, shift: int) -> str:
    result = []

    for ch in s:
        if ch.isalpha():
            base = ord("A") if ch.isupper() else ord("a")
            new_char = chr((ord(ch) - base + shift) % 26 + base)
            result.append(new_char)
        else:
            result.append(ch)

    return "".join(result)
