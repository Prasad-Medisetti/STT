#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 11:16:47 2019

@author: prasadm
"""
import itertools
import sys
#print(sorted(itertools.chain(eval(sys.argv[1:]))))

#print(sorted([int(x) for x in sys.argv[1:]]))

#print(sorted([int(x) for x in sys.argv[1:] if x.isdecimal()]))

l = []
for i in sys.argv[1:]:
    l+=eval(i)
print(l)
print(sorted(l))