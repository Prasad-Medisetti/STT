#l = [10, "ADITYA", True, 1+2j, 10.12]
#for i in l:
#    print(i, type(i),sep='\t')
l = [1, 1.5, 2, 2.5, 3, 3.5]
def types(l):
    li = []; lf = []
    for i in l:
        if type(i) == int:
            li.append(i)
        elif type(i) == float:
            lf.append(i)
    print(li, lf)
types(l)