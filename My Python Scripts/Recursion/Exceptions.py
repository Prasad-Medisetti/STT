# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 10:42:57 2019

@author: hp

topic: Exception Handling
"""

#Errors = [x for x in dir(__builtins__) if x.endswith('Error')]
#print(Errors)


class aditya(Exception):
    print('My Own Exception')

try:
    print('inner try')
    raise aditya
except aditya:
    print('aditya got raised')


#class aditya(Exception):
#    def __str__(self):
#        return 'aditya got raised'
#
#try:
#    print('inner try')
#    raise aditya
#except aditya as e:
#    print(e)