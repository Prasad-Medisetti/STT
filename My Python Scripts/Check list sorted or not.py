ls = [10,20,30]
ls1 = [30,20,10]
lus = [30,10,30]
def checkSorted(l,n):
    s = False
    rs = False
    i=0
    while i < n:
        if i+1 <= n-1:
            if l[i] < l[i+1]:
                s = True
            if l[i] > l[i+1]:
                rs = True
        i += 1    
    if s==True and rs==True:
        s=False
        rs=False
        print("Not sorted")
    else:
        print("Ascending :",s,'\t',"Descending :",rs)    
checkSorted(ls,len(ls))
checkSorted(ls1,len(ls1))
checkSorted(lus,len(lus))
