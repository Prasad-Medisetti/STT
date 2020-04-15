# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 10:31:08 2019
@author: hp

files
"""
#with open('hello.txt') as f:
#    ch = f.read(1)
#    while ch:
#        print(ch)
#        ch = f.read(1)
#    f.close()

#with open('Data.txt') as f:
#    for lineno,line in enumerate(f,1):
#        print(lineno,line,end='')
#        

#from string import ascii_letters
#l = []
#with open('Data.txt') as f:
#    data = f.read()
#    for i in ascii_letters:
#        l.append((i,data.count(i)))
#print('Most Repeated Char :',max(l,key=lambda x:x[1])[0])


#file copy
#f = open('hello.txt')
#f1 = open('write.txt','w')
#d = f.read()
#f1.write(d)
#f1.close()
#f.close()

f = open('Data.txt')
for line in f:
    print(line,file=f1)