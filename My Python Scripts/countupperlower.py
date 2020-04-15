s = input()
u = 0; l = 0
for char in s:
    if char.isupper():
        u += 1
    elif char.islower():
        l += 1
print("UPPER :", u, '\t', "LOWER :", l)