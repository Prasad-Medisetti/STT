# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 04:39:47 2019

@author: hp
"""

#def minion_game(s):
#    vowel = list('AEIOU')
#    K,S = 0,0
#    sub = (s[i:] for i in range(len(s)) for j in range(i+1,len(s)+1))
#    
#    while True:
#        try:
#            ns = next(sub)
#            if ns[0] in vowel:
#                K += 1
#            else:
#                S += 1
#        except StopIteration:
#            break
#    if S>K:
#        print('Stuart {}'.format(S))
#    elif K>S:
#        print('Kevin {}'.format(K))
#    elif S==K:
#        print('Draw')
def minion_game(s):
    vowels = list('AEIOU')
    n = len(s)
    K,S = 0,0
    for i in range(n):
        if s[i] in vowels:
            K += n-i
        else:
            S += n-i
        
    if S>K:
        print('Stuart {}'.format(S))
    elif K>S:
        print('Kevin {}'.format(K))
    elif S==K:
        print('Draw')
minion_game(input())