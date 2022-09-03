def isValid( s: str) -> bool:
    if len(s)%2:
        return False
    elif s[0] == ")" or s[0] == "]" or s[0] == "}" or s[-1] == "(" or s[-1] == "[" or s[-1] == "{":
        return False
    elif :
    else:
        for index in range(len(s)):
            if s[index] == "(" :
                for index2 in range(index + 1, len(s)):
                    if s[index2] == "(" or s[index + 1] == "]" or s[index + 1] == "}":
                        return False
            elif s[index] == "[" :
                for index2 in range(index + 1, len(s)):
                    if s[index2] == "[" or s[index + 1] == ")" or s[index + 1] == "}":
                        return False            
            elif s[index] == "{":
                for index2 in range(index + 1, len(s)):
                    if s[index2] == "{" or s[index + 1] == ")" or s[index + 1] == "]":
                        return False
        return True



solution = isValid("()")
print(solution)

solution = isValid("(]")
print(solution)

solution = isValid("()))")
print(solution)

solution = isValid("[)")
print(solution)

solution = isValid("()[]{}")
print(solution)

solution = isValid("{()}")
print(solution)

# solution = isValid(["reflower","flow","flight"])
# print(solution)