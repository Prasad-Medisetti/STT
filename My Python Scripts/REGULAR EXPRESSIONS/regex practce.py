#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 11:20:42 2020

@author: prasadm

REGEX practice
"""

# 1. a-zA-Z0-9
# 2. first char lower and in a-k
# 3. 2nd char digit and divisible by 3
# 4. length atleast 2


#import re as r
#s = input('Enter a string : ')
#l = r.match('^[a-k][0369][a-zA-Z0-9#]*',s)
#print(l) if l else print('Invalid')

s = input('Enter a Number of 10 digits : ')
l = r.fullmatch('[789]\d{9}',s)
print(l.group()) if l else print('Invalid')