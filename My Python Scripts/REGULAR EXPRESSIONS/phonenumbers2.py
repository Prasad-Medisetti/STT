from re import *
s = input('Enter Mobile Number : ')
m = fullmatch('(0|91)?[7-9][0-9]{9})', s)
if m != None:
    print('Valid Number')
else:
    print('Invalid Number')
