#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 15:17:34 2020

@author: prasadm
DATA STRUCTURES - STACK 
"""
#
#class stack:
#    '''This class is the implementation of Stack Data Structure'''
#    def __init__(self,size=50):
#        self.ds = []
#        self.top = -1
#        self.size = size
#        print('Stack Created with size %d'%self.size)
#    def push(self,ele):
#        if self.top == self.size-1:
#            print('STACK OVERFLOW...')
#            return
#        else:
#            self.ds.append(ele)
#            self.top += 1
#    def pop(self):
#        if self.size == -1:
#            print('STACK UNDERFLOW...')
#            return []
#        else:
#            ele = self.ds[self.top]
#            del self.ds[self.top]
#            self.top -= 1
#            return ele
#    def show(self):
#        print('Stack From TOP to BOTTOM')
#        for i in range(self.top, -1, -1):
#            print(self.ds[i],end=' ')
#        else:
#            print('Stack Underflow')
#    def __str__(self):
#        return 'Stack with size %s'%self.size
#    
    

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
    s = stack()
    st = input()
    post = ''
    d = {'+':1, '-':1, '*':2, '/':2}
    for i in st:
        if i not in d.keys():
            post += i
        else:
            ss = s.top()
            while ss and d[ss]>=d[i]:
                post += s.pop()
                ss = s.top()
            s.push(i)
    else:
        x = s.pop()
        while x:
            post += x
            x = s.pop()
    print(post)
    
    
#    s = stack(5)
#    print(s)
#    s.push(10)
##    s.push(20)
##    s.push(30)
#    s.show()
#    print(s.pop())
#    s.show()
    
#    st = 'Prasad'
#    print(st)
#    s = stack(len(st))
#    for i in st:
#        s.push(i)
#    while True:
#        k = s.pop()
#        if k:
#            print(k)
#        else:
#            break
    
#    st = input()
#    br = {')':'(',']':'[','}':'{'}
#    s = stack()
#    for i in st:
#        if i in br.keys():
#            s.push(i)
#        else:
#            x = s.pop()
#            if not x or x != br[i]:
#                print('Not Balanced')
#                break
#    else:
#        x = s.pop()
#        print('Balanced') if not x else print('Not Balanced')
    
    
#    st = 'abcZcba'
#    s = stack()
#    z = False
#    for i in st:
#        s.push(i)
    
#    st = '(())(())'
#    print(st)
#    s = stack(len(st))
#    for i in st:
#        if i=='(':
#            s.push(i)
#        else:
#            s.pop()
#    if s.top==-1:
#        print('Balanced')
#    else:
#        print('Unbalanced')