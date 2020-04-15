# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 14:11:50 2020

@author: hp
"""

'''

check if a string has all characters with same frequency with one variation allowed..

given a string of lowercase alphabets , find if it can be converted to a valid string by removing 1 or 0 characters . A "valid" string is a string str such that for all distinct characters in str each such character occurs the  same number of times in it.

Examples:

input: string str = "aabbcc"

output = valid string

input: string str = "abbca"

output : make it valid 

we can make it valid by removing 1 character

input: string str = "aabbcd"

output: not valid

we need to remove at least two characters to make it valid



For example:

Test	Input	Result
1       aabbcc  valid string
2       abbac   make it valid 
3
aabbcd
not valid
not valid

'''

# def valid(s):
    # u
#     valid = ''
#     for i in set(s):
#         if d[i]==2:
#             valid = 'valid string'
#         elif list(d.values()).count(1)==1:
#             valid = 'make it valid'
#         else:
#             valid = 'not valid'
#     return valid

# if __name__=="__main__":
#     s = input()
#     print(valid(s))
    





def valid(s):
    d = dict.fromkeys(s,0)
    for i in s:
        d[i] = d.get(i,0) + 1
    valid = False
    c1 = 1
    for i in d.keys():
        if d[i]==2:
            valid = True
            continue
        elif d[i]==1 and c1>0:
            valid = True
            c1 -= 1
            continue
        else:
            valid = False
    if valid==True:
        return 'valid string'
    elif valid==True and c1>=0:
        return 'make it valid'
    else:
        return 'not valid'

if __name__=="__main__":
    s = input()
    print(valid(s))