# 1st Problem
#s = input("Enter a string: ")
#ns = ''
#for i in range(0,len(s)):
#    ns+=(s[i]+str(list(s[:i+1]).count(s[i])))
#print(ns)


# 2nd Problem
#s = input("Enter a string: ")
#n = int(input("Enter index: "))
#print(s[n],':',s[n+1:].count(s[n]))


# 3rd Problem
n = int(input("Enter range: "))
s = int(input("Enter start: "))
sk = int(input("Enter skip count: "))
l = list(range(1,n))
seq = []
while l.count(-1) != len(l):
    if l[s] == -1:
        s += 1
    else:
        seq.append(l[s])
        l[s] = -1
        s = (s+sk)%len(l)
print(seq)