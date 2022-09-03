def isValid( s: str) -> bool:
    if len(s)%2:
        return False
    else:
        for index in range(0, len(s), 2):
            if s[index] == "(":
                if ord(s[index+1]) != ord(s[index]) + 1:
                    return False
            elif ord(s[index+1]) != ord(s[index]) + 2:
                return False
        return True



solution = isValid("()")
print(solution)

solution = isValid("(]")
print(solution)

solution = isValid("()[]{}")
print(solution)

solution = isValid("{()}")
print(solution)

# solution = isValid(["reflower","flow","flight"])
# print(solution)