l = list(range(1,11))
s = int(input("Enter Start: "))
e = int(input("Enter End: "))
print("List",l)
l[s:e] = sorted(l[s:e], reverse=True)
print(l)

# Another Way

#l = list(range(1,11))
#s = int(input("Enter Start: "))
#e = int(input("Enter End: "))
#print("List",l)
#print(l[:s]+sorted(l[s:e], reverse=True)+l[e:])