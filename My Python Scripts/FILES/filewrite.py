# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 09:06:56 2019
@author: hp

file write with reversed words of ip
"""


#with open('write.txt','w') as f:
#    with open('Data.txt') as fr:
#        for line in fr.readlines():
#            for word in line.split():
#                print(word[::-1],end=' ',file=f)
#            print(file=f)

         
#with open('write1.txt','w') as f:
#    with open('Data1.txt') as fr:
#        s = 0
#        for line in fr.readlines():
#            for w in line.split():
#                if w.isdigit():
#                    s += int(w)
#                elif w.isalnum():
#                    wn = ''
#                    for i in w:
#                        if i.isalpha():
#                            wn += i
#                    print(wn,file=f,end=' ')
#            print(file=f)
#        print(str(s),file=f)
#        
with open('write2.txt','w') as fw:
    with open('Data.txt') as f:
        with open('Data1.txt') as fr:
            d1 = f.readlines()
            d2 = fr.readlines()
            for i,j in zip(d1,d2):
                print(i,file=fw,end='')
                print(j,file=fw,end='')
            