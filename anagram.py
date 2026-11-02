def anagram(s1: str, s2: str) -> bool:
    str1 = sorted(s1.lower().replace(" ", ""))
    str2 = sorted(s2.lower().replace(" ", ""))

    if str1 == str2:
        return True
    else:
        return False


if __name__ == "__main__":
    print(anagram("listen", "silent"))
    print(anagram("Triangle", "Integral"))
    print(anagram("Dormitory", "Dirty Room"))
    print(anagram("hello", "world"))
    print(anagram("", ""))
    print(anagram("abc", "abcc"))