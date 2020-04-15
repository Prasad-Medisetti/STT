# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 12:14:52 2019

@author: hp
"""
s = """Python is a widely used general-purpose, high level programming language.
It was initially designed by Guido van Rossum in 1991 and developed by Python Software Foundation.
It was mainly developed for emphasis on code readability, and its syntax allows programmers to 
express concepts in fewer lines of code.
Python is a widely used general-purpose, high level programming language. It was initially designed by Guido van Rossum in 1991 and 
developed by Python Software Foundation. It was mainly developed for emphasis on code readability, 
and its syntax allows programmers to express concepts in fewer lines of code."""
d = {}
#for word in s.split():
#    d[word] = d.get(word,0) + 1
#print(d)
d = {}
for lno,line in enumerate(s.split(),start=1):
    for word in line.split():
        d.setdefault(word,[]).append(lno)
        
        
# =============================================================================
# def add(*l,**d):
#     print('Sum of',*l,':',sum(l))
#     if len(d) > 0:
#         print('Sum of',*list(zip(list(d.keys()),list(d.values()))),':',sum(list(d.values())))
# =============================================================================
