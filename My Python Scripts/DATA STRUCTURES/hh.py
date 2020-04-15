#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 15:22:43 2020

@author: prasadm
"""
import re
s = input();stri=""
date = re.search('\d{2}[st|nd|rd|th]{2}\s\w+\s\d{4}',s).group(0)
time = re.search('\d\d:\d\d\s?[PM|AM]*',s).group(0)
#st=re.findall(r"[A-Z][a-z]+|[a-z]+|[A-Z]+",s)
str1 = re.findall(r'[A-Z][a-z]+|[a-z]+|[A-Z]+',s)
if 'PM' in time or 'AM' in time:
    h,r = time.split()[0].split(':')
    time = str(int(h)+12)+':'+r
print(*[i for i in str1 if len(i)>3 or i.isupper() and len(i)>2],'-',date,time)