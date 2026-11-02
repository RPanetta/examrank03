def whisper_cipher(text: str, shift: int) -> str:
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    
    for char in text:
        new_char = char
        for i in range(26):
            if char == lower[i]:
                new_char = lower[(i + shift) % 26]
            elif char == upper[i]:
                new_char = upper[(i + shift) % 26]
        result += new_char
    return result


if __name__ == "__main__":
    print(whisper_cipher("hello", 3))
    print(whisper_cipher("Hello World!", 1))
    print(whisper_cipher("xyz", 3))
    print(whisper_cipher("ABC123def", 5))
    print(whisper_cipher("", 10))
    print(whisper_cipher("abc", -3))
