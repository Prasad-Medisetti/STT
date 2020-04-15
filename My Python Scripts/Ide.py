# # cook your dish here
for i in range(1,10):
    f=0
    for j in range(1,i//2):
        if j%i==0:
            f+=1
    if f==2:
        print(i,end=' ')
# l = []
# for i in range(100,9001):
#     if i%7==0:
#         l.append(i)
# print(sum(l))