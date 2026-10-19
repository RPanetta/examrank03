def bracket_validator(s: str) -> bool:
    opener = "([{"
    closer = ")]}"
    stack = ""

    for char in s:
        if char in opener:
            stack += char
        elif char in closer:
            if stack and opener[closer.index(char)] == stack[-1]:
                stack = stack[:-1]
            else:
                return False

    if len(stack) > 0:
        return False
    return True


print(bracket_validator("()"))
print(bracket_validator("()[]{}"))
print(bracket_validator("(]"))
print(bracket_validator("([)]"))
print(bracket_validator("{[]}"))
print(bracket_validator("hello(world)"))
print(bracket_validator("((())"))
print(bracket_validator(""))


#def bracket_validator(s: str) -> bool:
#    open_bracket = {"(", "{", "["}
#    stack = []
#    closed_bracket = {")", "}", "]"}
#    match = {"]": "[" , "}": "{", ")": "("}

#    for ch in s:
#        if ch in open_bracket:
#            stack.append(ch)
#        elif ch in closed_bracket:
#            if not stack or stack.pop() != match[ch]:
#                return False
           
#    return len(stack) == 0


#if __name__ == "__main__":
#    print(f"True -> {(bracket_validator("()"))}")
#    print(f"True -> {(bracket_validator("()[]{}"))}")
#    print(f"False -> {(bracket_validator("(]"))}")
#    print(bracket_validator(""))
