# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 10:05:41 2019
@author: hp
"""

from csv import reader
with open('html table.html','w') as fw:
    with open('csv file1.csv') as fr:
        data = reader(fr)
        l = ['<table border=1 width=200px>\n']
        for row in data:
            l.append('<tr>\n')
            for col in row:
                l.append('<td>%s</td>\n'%col)
            l.append('</tr>\n')   
        l.append('</table>')         
    fw.writelines(l)