import string
cnt = {}
s = input("Enter a String :\t")
for i in string.ascii_letters:
    cnt[i] = s.count(i)
for i in string.ascii_letters:
    if cnt[i] != 0:
        print(i, ':', cnt[i])