l = [1, 2, 3, 4, 5, 6, 1, 2, 3]
unq = []; dup =[]
for i in range(0, len(l)):
    if l[i] not in unq:
        unq.append(l[i])
    else:
        dup.append(l[i])
print(unq, dup, sep='\t')