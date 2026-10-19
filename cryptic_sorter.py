#def cryptic_sorter(strings: list[str]) -> list[str]:
#    result = []
#    keys = []

#    for text in strings:
#        lower = text.lower()
#        vowels = 0
#        for char in lower:
#            if char in "aeiou":
#                vowels += 1
#        key = (len(text), lower, vowels)

#        position = len(result)
#        while position > 0 and keys[position - 1] > key:
#            position -= 1

#        result.insert(position, text)
#        keys.insert(position, key)

#    return result


def sorting(a: str, b: str) -> bool:
    if len(a) != len(b):
        return len(a) > len(b)
    if a.lower() != b.lower():
        return a.lower() > b.lower()
    return False


def cryptic_sorter(strings: list[str]) -> list[str]:
    n = len(strings)

    for first in range(n):
        for second in range(first + 1, n):
            if sorting(strings[first], strings[second]):
                strings[first], strings[second] = strings[second], strings[first]
    return strings


if __name__ == "__main__":
    test_a = ["apple","cat","banana","dog","elephant"]
    test_b = ["aaa","bbb","AAA","BBB"]
    test_c = ["hello","world","hi","test"]
    test_d = [[]]
    test_e = [""]

    print(cryptic_sorter(test_a))
    print(cryptic_sorter(test_b))
    print(cryptic_sorter(test_c))
    print(cryptic_sorter(test_d))
    print(cryptic_sorter(test_e))
