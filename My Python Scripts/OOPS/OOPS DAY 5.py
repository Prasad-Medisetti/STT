#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 19:31:40 2020

@author: prasadm

ABSTRACT CLASSES - DIAMOND PROBLEM
"""

#from abc import ABC, abstractmethod

#class details:
#    l = []
#    def __init__(self,name,pno):
#        self.name = name
#        self.pno = pno
#        details.l.append(self)
#    def show_details(self):
#        return details.l
#class mail:
#    def sendmail(self):
#        return print('Sending email to',self.email)
#class friends(details,mail):
#    def __init__(self,name,pno,email):
#        super().__init__(name,pno)
#        self.email = email
#f = friends('P',34,'P@M')
#f.sendmail()
#print(f.show_details())

#
#class base:
#    nbc = 0
#    def callme(self):
#        print("base class")
#        base.nbc += 1
#    
#class leftsubclass(base):
#    nlc = 0
#    def callme(self):
##        base.callme(self)
#        super().callme()
#        print("left subclass")
#        leftsubclass.nlc += 1
#        
#class rightsubclass(base):
#    nrc = 0
#    def callme(self):
##        base.callme(self)
#        super().callme()
#        print("right subclass")
#        rightsubclass.nrc += 1
#        
#class sample(leftsubclass, rightsubclass):
#    ns = 0
#    def callme(self):
#        super().callme()
#        print("Sample class")
#        sample.ns += 1
#s = sample()
#s.callme()
#print(base.nbc,leftsubclass.nlc,rightsubclass.nrc,sample.ns)





#class A:
#    def __init__(self,a=0,**kw):
#        print("Arguments in A : ",kw)
#        super().__init__(**kw)
#        self.a = a
#    def show(self):
#        return self.a
#        
#class B:
#    def __init__(self,b=0,**kw):
#        print("kw in : B ",kw)
#        super().__init__(**kw)
#        self.b = b
#    def show(self):
#        return self.b
#
#class C(A,B):
#    def __init__(self,c=0,**kw):
#        print("kw in : C ",kw)
#        super().__init__(**kw)
#        self.c = c
#    def show(self):
#        return self.a+self.b+self.c
#
#c = C(a=23,c=34,b=45)
#print(C.__mro__)
#c = C(a=23,c=34,b=45,d=55,f=67)

# =============================================================================
# start and end same
# s = 'amadam'; n = ''
# for i in range(len(s)-1):
#     if s.endswith(s[:i+1]):
#         n += s[:i+1]
# print(n)
# =============================================================================




strclass Table:
    def __init__(self):
        self.nooflegs = 4
        self.glasstop = None
        self.woodentop = None
dtable = Table()
btable = Table()
ftable = btable
btable = dtable
print(dtable,btable,ftable,sep='\n')