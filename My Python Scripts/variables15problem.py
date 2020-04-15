t = ['SL','LB','MB','UB','LB','MB','UB','SU']
n = int(input())
if n>0:
    if n%8==0 or n%8==7:
        if n%8==0:
            print(str(n-1)+t[n%8]) 
        else:
            print(str(n+1)+t[n%8])
    elif n%8==1:
        print(str(n+3)+t[n%8])
    elif n%8==2:
        print(str(n+3)+t[n%8])
    elif n%8==3:
        print(str(n+3)+t[n%8])
    elif n%8==4:
        print(str(n-3)+t[n%8])
    elif n%8==5:
        print(str(n-3)+t[n%8])
    elif n%8==6:
        print(str(n-3)+t[n%8])