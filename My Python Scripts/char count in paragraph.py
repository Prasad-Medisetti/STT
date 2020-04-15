# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 09:43:16 2019
@author: hp
"""
from string import ascii_letters
s = """Python is a widely used general-purpose, 
high level programming language.
It was initially designed by Guido van Rossum in 1991 and 
developed by Python Software Foundation.
It was mainly developed for emphasis on code readability, 
and its syntax allows programmers to 
express concepts in fewer lines of code."""
d = {}
for i in s:
    if i in ascii_letters:
        d[i] = d.get(i,0) + 1
        #d[i] = d.setdefault(i,0) + 1
print(d)
#d = {i:s.count(i) for i in ascii_letters}    
#l = sorted(d.values(),reverse=True)
#print(max(d.items(), key=lambda x:x[1]))
#print(min(d.items(), key=lambda x:x[1]))