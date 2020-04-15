# functools module
from functools import reduce
l = list(range(1,11))
print(reduce(lambda x,y : x+y, l))