# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 12:12:53 2019

@author: hp

DUCCI SEQUENCE
A Ducci sequence is a sequence of lists of integers. Given a starting list of integers, the next list in the sequence is formed by taking the absolute differences of neighboring integers in the previous list.Start List: [0,653,1854,4063]

Ducci Sequence:[653,1201,2209,4063], [548,1008,1854,3410], ...........,[0,0,0,0]

Assumption: The Ducci sequence ends with a list containing 0s and the starting list contains four elements.
Ducci Sequence for start list [0,653,1854,4063] is

[653; 1201; 2209; 4063]
[548; 1008; 1854; 3410]
[460; 846; 1556; 2862]
[386; 710; 1306; 2402]
[324; 596; 1096; 2016]
[272; 500; 920; 1692]
[228; 420; 772; 1420]
[192; 352; 648; 1192]
[160; 296; 544; 1000]
[136; 248; 456; 840]
[112; 208; 384; 704]
[96; 176; 320; 592]
[80; 144; 272; 496]
[64; 128; 224; 416]
[64; 96; 192; 352]
[32; 96; 160; 288]
[64; 64; 128; 256]
[0; 64; 128; 192]
[64; 64; 64; 192]
[0; 0; 128; 128]
[0; 128; 0; 128]
[128; 128; 128; 128]
[0; 0; 0; 0]

Write a python function that takes a starting list of integers and a number ‘n’ as input, and returns the nth element of the Ducci sequence.

Sample Input	Expected Output
[0,653,1854,4063]
1	[548, 1008, 1854, 3410]
"""

def ducciSequence(inputs,limit):
    f = 0
    for i in range(limit+1):
        for j in range(len(inputs)):
            if j==0:
                f = inputs[j]
                inputs[j] = abs(inputs[j+1]-inputs[j])
            elif j==len(inputs)-1:
                inputs[j] = abs(inputs[j]-f)
            else:
                inputs[j] = abs(inputs[j+1]-inputs[j])
    return inputs

if __name__ == '__main__':
    inputs = [int(x) for x in input().split()]
    limit = int(input())
    print(ducciSequence(inputs,limit))