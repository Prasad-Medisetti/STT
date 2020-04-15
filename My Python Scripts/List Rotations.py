l = list(range(1,11))
print("Original List",l)
n = int(input("Enter an integer: "))
#n %= len(l)
print("List After Right Rotaion by %d"%n,l[len(l)-n:]+l[:len(l)-n])
print("List After Left Rotaion by %d"%n,l[n:]+l[:n])
# Another Method
# print("List After Left Rotaion by %d"%n,l[n%len(l):]+l[:n%len(l)])