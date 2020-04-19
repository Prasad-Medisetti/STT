# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 16:30:52 2020

@author: hp
"""

'''

Read a string, in that string, at last, there are some spaces, then we have to adjust that last spaces in word spaces in that string.

here for our convenience space is represented with _(underscore)

Sample input:

this_is_sudhir___

Sample Ouput:

this___is__sudhir



For example:

Test	Input                             Result
1       this_is_sudhir___                 this___is__sudhir
2       this_is_Python_Class              this_is_Python_Class
3       Aditya_Engineering_college_______ Aditya_____Engineering____college

'''


# def AdjustUnderscores(s):
#     if s[-1]=='_':
#         underscores = s.count('_')
#         words = [word for word in s.split('_') if word]
#         ns = ''
#         l = len(words)
#         for i in range(l,0,-1):
#             if underscores%l:
#                 ns += words[l-i]+'_'*(underscores%l)
#                 underscores -= i
#             if underscores==0:
#                 ns += words[-1]
#                 break
#     else:
#         ns = s
#     return ns

# s = input()
# print(AdjustUnderscores(s))


#Python code
st=input()
l=list(st)
l.reverse()
sp=0
for i in l:
    if i=="_":
        sp=sp+1
        
    else:
        break
l.reverse()
l=l[:len(l)-sp]
i=0
s=1
k=2# imp value
while s<=sp:
    if l[i]=="_":
        #print(i)
        #print(l)
        l.insert(i+1,"_")
        i=i+k
        s=s+1
    else:
        i=i+1
    if i==len(l)-1:
        i=0
        k=k+1
    
s=''.join(l)
print(s)
#Author : Sudhir