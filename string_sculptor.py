def string_sculptor(text: str) -> str:
    next_is_lower = True
    result = ""

    for char in text:
        if char.isalpha():
            if next_is_lower:
                result += char.lower()
            else:
                result += char.upper()
            next_is_lower = not next_is_lower
        else:
            result += char
    return result


if __name__ == "__main__":
    print(string_sculptor("hello"))
    print(string_sculptor("Hello World"))
    print(string_sculptor(" hello "))
    print(string_sculptor("abc123def"))
    print(string_sculptor("Python3.9!"))
    print(string_sculptor(""))