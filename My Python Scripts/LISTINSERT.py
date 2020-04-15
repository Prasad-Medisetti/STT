l = []
while True:
    ele = int(input("Enter Element :\t"))
    pos = int(input("Enter Position :\t"))
    if pos > len(l):
        for i in range(len(l), pos-1):
            l.insert(i, 0)
        l.insert(pos, ele)
    else:
        l[pos-1] = ele
    print(l)
    ch = input("Do you want to continue(0/1): ")
    if ch == '1':
        break