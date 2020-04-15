#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 14:56:48 2020

@author: prasadm
"""
# subsets of list
from itertools import *
def subsets(l):
    subsets = []
    for i in range(1, len(l)+1):
        subsets.extend([tuple(x) for x in combinations(l,i)])
    return subsets
print(*subsets([1,2,3]),sep='\n')

#sumL = int(input())
#for i in subsets([int(x) for x in input().split()]):
#    if sum(i)==sumL:
#        print(i)

		
# Subsets of String
#def subsets(s,l):
#	return sorted([s[i:len] for i in range(l) for len in range(i+1,l+1)],key=lambda x:len(x))
#s = input()
#print(*subsets(s,len(s)),sep='\n')
