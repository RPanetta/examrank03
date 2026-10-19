def echo_validator(text: str) -> bool:

    reverse_text = text[::-1]

    if text:
       return text.replace(" ", "").lower() == reverse_text.replace(" ", "").lower()
    return False


print(echo_validator("racecar"))
print(echo_validator("A man a plan a canal Panama"))
print(echo_validator("race a car"))
print(echo_validator("Was it a car or a cat I saw"))
print(echo_validator("hello"))
print(echo_validator("Madam Im Adam"))
print(echo_validator("madam"))
print(echo_validator("Able was I ere I saw Elba"))
print(echo_validator(""))
