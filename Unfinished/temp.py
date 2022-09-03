def isValid( s: str) -> bool:
    list = []
    list[:0] = s
    for _ in range(len(list)):
        if list == []:
            return True
        elif list[0] == "(":
            list.pop(0)
            try:
                list.remove(")")
            except:
                return False
        elif list[0] == "{":
            list.pop(0)
            try:
                list.remove("}")
            except:
                return False
        elif list[0] == "[":
            list.pop(0)
            try:
                list.remove("]")
            except:
                return False
        else:
            return False


solution = isValid("([)]")
print(solution)

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