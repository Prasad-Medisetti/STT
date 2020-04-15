#l = []
#while 1:
#    e = input("Enter 'stop' to stop entering numbers:\t")
#    if e == 'stop':
#        break
#    else:
#        l.append(int(e))
#print(l)
l1 = []; l = []
#[l1.append(int(i)) for i in input().split()]
for i in input().split():
    l1.append(int(i))
for i in range(1, len(l1)):
    l1[i] = l1[i - 1] + l1[i]
print(l1)
#    if i == 0:
#        l.append(l1[i])
#    elif i+1 <= len(l1):
#        e = l[len(l)-1] + l1[i]
#        l.append(e)
#print(l)