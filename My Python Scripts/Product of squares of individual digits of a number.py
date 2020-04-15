# Product of squares of individual digits of a number
from functools import reduce
n = input("Enter an integer: ")
print(reduce(lambda x,y : x**2*y**2 ,[int(x) for x in n]))



#l = [1,2,3,4,5]
#[(x,y) for x in l for y in l if x != y]
#[(1, 2),
# (1, 3),
# (1, 4),
# (1, 5),
# (2, 1),
# (2, 3),
# (2, 4),
# (2, 5),
# (3, 1),
# (3, 2),
# (3, 4),
# (3, 5),
# (4, 1),
# (4, 2),
# (4, 3),
# (4, 5),
# (5, 1),
# (5, 2),
# (5, 3),
# (5, 4)]