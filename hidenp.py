def hidenp(small: str, big: str) -> bool:
    count = 0
    i = 0
    for char in big:
        if count < len(small) and char == small[i]:
            count += 1
            i += 1
    return count == len(small)


if __name__ == "__main__":
    print(hidenp("abc", "a1b2c3"))
    print(hidenp("ace", "abcde"))
    print(hidenp("aec", "abcde"))
    print(hidenp("", "abc"))
    print(hidenp("abc", "ab"))
    print(hidenp("aaaa", "aaa"))
    print(hidenp("sing","subsequence testing"))
