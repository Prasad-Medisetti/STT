# =============================================================================
# read 2 strings
# print chars in common the form of string 
# =============================================================================
s1 = input()
s2 = input()
sc = ''
sc1 = ''
sc2 = ''
for c in s1:
    if c == ' ':
        continue
    elif  c in s2 and c not in sc:
        sc += c
        continue
    elif c not in sc:
        sc1 += c
for c in s2:
    if c == ' ':
        continue
    elif c not in sc:
        sc2 += c
print("COMMON :",sc)
print("S1 :",sc1)
print("S2 :",sc2)