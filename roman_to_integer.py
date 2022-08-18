s = "MCMXCIV"
s = s.lower()
result = 0
integer = list()
rom2int = {'i':1, 'v': 5, 'x':10,'l':50,'c':100,'d':500, 'm':1000}
for roman in s: integer.append(rom2int[roman])
print (integer)
while integer:
    if len(integer) >= 2:
        if integer[0] < integer[1]:
            result = (integer[1] - integer[0]) + result
            integer.pop(0)
            integer.pop(0)
        else:
            result = result + integer[0]
            integer.pop(0)
    else:
        result = result + integer[0]
        integer.pop(0)
print(result)
