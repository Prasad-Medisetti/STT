import string
s1 = string.ascii_lowercase
s2 = input()
n = int(input())
ns = ''
for c in s2:
    if c in s1:
        i = s1.index(c)
        ni = (i + n) % 26
        ns = ns + s1[ni]
    else:
        ns = ns + c
print(ns)