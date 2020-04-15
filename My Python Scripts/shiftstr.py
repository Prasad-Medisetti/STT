s = input("Enter a String :\t")
n = int(input("Enter shift value :\t"))
s1 = ''
for ch in s:
    if ch.isalpha():
        if ord(ch) + n <= 122:
            s1 += chr(ord(ch) + n)
        else:
            s1 += chr(96 + n)
    else:
        s1 += ch
print(s1)