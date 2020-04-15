from re import *
s = input('Enter email : ')
m = fullmatch('[a-z][a-zA-Z0-9_.]*@gmail[.]com', s)
if m != None:
    print('Valid Email')
else:
    print('Invalid Email')
