#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 19:31:40 2020

@author: prasadm

ABSTRACT CLASSES
"""

from abc import ABC, abstractmethod

#class polygon(ABC):
#    @abstractmethod
#    def area(self):
#        pass
#    @abstractmethod
#    def perimeter(self):
#        pass
#    @classmethod
#    def m(self):
#        print('Not an abstract method...')
#
#class rectangle(polygon):
#    def __init__(self,side):
#        self.side = side
#    def area(self):
#        return self.side*self.side
#    def perimeter(self):
#        return self.side*4
#        
#p = rectangle(10)
#print(p.area())
#print(p.perimeter())
#p.m()

#class point:
#    def __init__(self,x,y):
#        self.x = x
#        self.y = y
#    def xy(self):
#        return (self.x,self.y)
#class polygon:
#    def __init__(self):
#        self.points = []
#    def addpoint(self,p):
#        self.points.append(p)
#    def showpoints(self):
#        for p in self.points:
#            print(p.xy())
#p = point(2,3)
#rect = polygon()
#rect.addpoint(p)
#rect.addpoint(point(3,2))
#rect.addpoint(point(4,2))
#rect.addpoint(point(2,4))
#rect.showpoints()

class details:
    l = []
    def __init__(self,name,pno):
        self.name = name
        self.pno = pno
        details.l.append(self)
    def show_details(self):
        return details.l
class mail:
    def sendmail(self):
        return print('Sending email to',self.email)
class friends(details,mail):
    def __init__(self,name,pno,email):
        super().__init__(name,pno)
        self.email = email
f = friends('P',34,'P@M')
f.sendmail()
#print(f.show_details())