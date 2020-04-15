#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 14:48:00 2020

@author: prasadm

DATA STRUCTURES - STACK 
"""

class queue:
    '''This class is the implementation of Queue Data Structure'''
    def __init__(self, size = 50):
        self.ds = []
        self.size = size
        print('Queue Created with size %d'%self.size)
    
    def enqueue(self, value):
        if len(self.ds) == self.size:
            print('QUEUE OVERFLOW...')
            return
        else:
            self.ds.append(value)
            
    def dequeue(self):
        if len(self.ds) == 0:
            return []
        else:
            return self.ds.pop(0)
    
    def show(self):
        if len(self.ds) == 0:
            print('QUEUE UNDERFLOW')
            return []
        else:
            for i in range(len(self.ds)):
                print(self.ds[i],end=' ')
            print()
            
class queue1:
    '''This class is the implementation of Queue Data Structure'''
    def __init__(self, size = 50):
        self.ds = []
        self.size = size
        print('Queue Created with size %d'%self.size)
    
    def enqueue(self, value):
        if len(self.ds) == self.size:
            print('QUEUE OVERFLOW...')
            return
        else:
            self.ds.append(value)
            
    def dequeue(self):
        if len(self.ds) == 0:
            return []
        else:
            return self.ds.pop(0)
    
    def show(self):
        if len(self.ds) == 0:
            print('QUEUE UNDERFLOW')
            return []
        else:
            for i in range(len(self.ds)):
                print(self.ds[i],end=' ')
            print()
        
    def __str__(self):
        return 'Queue with size %s'%self.size
        
if __name__ == '__main__':
    q = queue(5)
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.show()
    print(q.dequeue())
    q.show()
    print(q.dequeue())
    q.show()    
    