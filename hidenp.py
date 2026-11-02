def hidenp(small: str, big: str) -> bool:
    i = 0
    for char in big:
        if i < len(small) and char == small[i]:
            i += 1
    return i == len(small)


if __name__ == "__main__":
    print(hidenp("abc", "a1b2c3"))
    print(hidenp("ace", "abcde"))
    print(hidenp("aec", "abcde"))
    print(hidenp("", "abc"))
    print(hidenp("abc", "ab"))
    print(hidenp("aaaa", "aaa"))
    print(hidenp("sing","subsequence testing"))
