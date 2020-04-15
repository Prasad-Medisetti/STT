# map and filter
l = list(range(1,11))

print(list(map(lambda x:x+1, l)))
print([x+1 for x in l])

print(list(filter(lambda x:x%2 == 0, l)))
print([x for x in l if x%2==0])