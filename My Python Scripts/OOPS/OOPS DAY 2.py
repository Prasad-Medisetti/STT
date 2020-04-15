#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 09:38:02 2020

@author: prasadm
"""

#class Person:
#    l = []
#    def __init__(self,name,no):
#        self.name = name
#        self.no = no
#        Person.l.append(self)
#    def show(self):
#        print(Person.l)


#class Student(Person):
#    def __init__(self,name,no,email):
#        super().__init__(name,no)
#        self.email = email
#    def register(self):
#    print('Yes, %s can register with email %s'%(self.name,self.email))


#class MyList(list):
#    def __getitem__(self,pos):
#        return 'item at {} is {}'.format(pos, super().__getitem__(pos))
#    def longest_item(self):
#        """Returns Longest String"""
#        s = ''
#        for i in self:
#            if type(i)==str and len(i)>len(s):
#                s = i
#        return s
#
#l = MyList()
#l.append('Prasad')
#l.append(5)
#l.append('HP')    


#class A:
#    def __init__(self,a):
#        self.a = a
#    def show(self):
#        return self.a
#
#class B(A):
#    def __init__(self,a,b):
#        super().__init__(a)
#        self.b = b
#    def show(self):
#        return self.a+self.b
#    
#class C(B):
#    def __init__(self,a,b,c):
#        super().__init__(a,b)
#        self.c = c
#    def show(self):
#        return self.a + self.b + self.c


class P:
    def __init__(self,name,no):
        self.name = name
        self.no = no
    def __eq__(self,obj):
        return self.no==obj.no    
    def __lt__(self,obj):
        return self.no<obj.no
    def __gt__(self,obj):
        return self.no>obj.no
    def s(self):
        return '{} {}'.format(self.name,self.no)
a = P('Raj',12)
b = P('Rani',13)
