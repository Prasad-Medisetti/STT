l = list(range(1,51))
odd = []
even = []
for i in range(0, len(l)):
    if i%2 == 0:
        even.append(l[i])
        continue
    odd.append(l[i])
#Another Way
#print(l[::2])
#print(l[1::2])
print(even)
print(odd)