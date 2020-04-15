#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 10:26:18 2020

@author: prasadm

REGULAR EXPRESSIONS
"""

import re as r

# ==================================================================
# \s ---- space
# \d ---- any digit in 0-9
# \D ---- any char except digit
# \w ---- any word char a-zA-Z0-9
# ===================================================================

#count = 0
#pattern = r.compile('ab')
#matcher = pattern.finditer('abaababa')
#for match in matcher:
#    count += 1
#    print(match.start(),match.end(),match.group())
#print(count)

#matcher = r.finditer('[abc]','a7b@k9z') 	# [abc] -- a or b or c
#for match in matcher:
#	print(match.start(),'....',match.group())

#matcher = r.finditer('[^abc]','a7b@k9z') 	# ^ -- except
#for match in matcher:
#	print(match.start(),'....',match.group())

#matcher = r.finditer('[a-z]','a7b@k9z')		# - -- range
#for match in matcher:
#	print(match.start(),'....',match.group())
	
#matcher = r.finditer('[0-9]','a7b@k9z')		# - -- range
#for match in matcher:
#	print(match.start(),'....',match.group())

#matcher = r.finditer('[\w]','a7b@ k9z')		# - -- range
#for match in matcher:
#	print(match.start(),'....',match.group())

#matcher = r.finditer('a{1,4}','abaabaaab ')		# {min,max} -- 
#for match in matcher:
#	print(match.start(),'....',match.group())

#matcher = r.finditer('$b','abaabaaab ')		# {min,max} -- 
#for match in matcher:
#	print(match.start(),'....',match.group())

#s = input('Enter a pattern to check: ') 		# input : ab
#m = r.match(s,'abcabdefg')
#if m!=None:
#	print(m.start(),'...',m.end(),m.group())
#else:
#	print('Match not Available')

#s = input('Enter a pattern to check: ') 		# input : abcabdefg
#m = r.fullmatch(s,'abcabdefg')
#if m!=None:
#	print(m.start(),'...',m.end(),m.group())
#else:
#	print('Match not Available')
	
#s = input('Enter a pattern to check: ') 		# input : ab
#m = r.search(s,'abcabdefg')
#if m!=None:
#	print(m.start(),'...',m.end(),m.group())
#else:
#	print('Match not Available')

#s = input('Enter a pattern to check: ') 		# input : ab
#m = r.findall(s,'abcabdefg')
#print(m)

#p = input('Enter a pattern to check: ') 		# input : ab
#s = input('Enter str to sub: ')				# input : 12
#st = 'abcabdefg'
#st = r.sub(p,s,st)
#print(st)

#p = input('Enter a pattern to check: ') 		# input : ab
#s = input('Enter str to sub: ')				# input : 12
#st = 'abcabdefg'
#st = r.subn(p,s,st)
#print(*st)

p = input('Enter a pattern to check: ') 		# input : ab
st = 'abcabdefg'
s1 = r.split(p,st)
print(s1)