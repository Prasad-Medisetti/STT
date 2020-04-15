#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 14:19:50 2020

@author: prasadm

DATA STRUCTURES - STACK 
"""

class stack:
    '''This class is the implementation of Stack Data Structure'''
    def __init__(self,size=50):
        self.ds = []
        self.size = size
        print('Stack Created with size %d'%self.size)
    def push(self,ele):
        if len(self.ds) == self.size-1:
            print('STACK OVERFLOW...')
            return
        else:
            self.ds.append(ele)
    
    def top(self):
        if len(self.ds)==0:
#            print('STACK UNDERFLOW...')
            return []
        else:
            return self.ds[-1]        
            
    def pop(self):
        if len(self.ds)==0:
#            print('STACK UNDERFLOW...')
            return []
        else:
            ele = self.ds.pop()
            return ele
        
    def show(self):
        print('Stack From TOP to BOTTOM')
        for i in range(self.top, -1, -1):
            print(self.ds[i],end=' ')
            
    def __str__(self):
        return 'Stack with size %s'%self.size
        

if __name__=='__main__':
    # INFIX to POSTFIX
#    s = stack()
#    st = input()
#    post = ''
#    d = {'+':1, '-':1, '*':2, '/':2}
#    for i in st:
#        if i not in d.keys():
#            post += i
#        else:
#            ss = s.top()
#            while ss and d[ss]>=d[i]:
#                post += s.pop()
#                ss = s.top()
#            s.push(i)
#    else:
#        x = s.pop()
#        while x:
#            post += x
#            x = s.pop()
#    print(post)
    
    
    # POSTFIX evaluation
    s = stack()
    post = input()
    d = {'+':1, '-':1, '*':2, '/':2}
    for i in post:
        if i not in d.keys():
            s.push(i)
        else:
            op2 = s.pop()
            op1 = s.pop()
            opr1 = s.pop()
            if 
            
            s.push(res)
    else:
        print(s.pop())