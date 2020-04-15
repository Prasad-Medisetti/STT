# import itertools as it
# # t = int(input())
# # l = []; pt=[]
# # if t >= 1 and t <= 100:
# #     for i in range(t):
# #         l.append([int(x) for x in input().split()])
# # n = ['1'*l[i][0]+'2'*l[i][1]+'3'*l[i][2]+'4'*l[i][3]+'5'*l[i][4]+'6'*l[i][5]+'7'*l[i][6]+'8'*l[i][7]+'9'*l[i][8] for i in range(9)]
# pt = list(it.permutations('336'))
# def check11(t):
#     osum = 0
#     esum = 0
#     n=len(t)
#     for i in range(0,n):
#         if i%2==0:
#             esum += int(t[i])
#         else:
#             osum += int(t[i])
#     return (osum - esum) % 11 == 0
# for i in range(0,len(pt)):
#     if check11(pt[i])==True:
#         print('Yes')


# # OUTPUT
# #l = [[0, 0, 2, 0, 0, 1, 0, 0, 0],
# # [0, 0, 0, 0, 0, 0, 0, 0, 12],
# # [0, 0, 0, 0, 2, 0, 1, 1, 0],
# # [3, 1, 1, 1, 0, 0, 0, 0, 0],
# # [3, 0, 0, 0, 0, 0, 3, 0, 2],
# # [0, 0, 0, 0, 0, 0, 0, 1, 0]]
# #print(n)
# #['336', '999999999999', '5578', '111234', '11177799', '8']



from itertools import permutations
lst = []
perm = []
n = int(input())
for i in range(n):
    lst.append(input().split())
for i in range(n):
    perm.append(list(permutations(lst[i])))
for i in range(n):
    for j in list(perm[i]):
        s = ''.join(list(j))
        if int(s) % 11 == 0:
            print('Case #{}: YES'.format(i+1))
            break
        else:
            print('Case #{}: NO'.format(i+1))
