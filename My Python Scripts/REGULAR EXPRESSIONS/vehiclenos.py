from re import *
s = input('Enter Vehicle Registration Number : ')
m = fullmatch('AP[012][0-9][A-Z]{2}\d{4}', s)
if m != None:
    print('Valid Vehicle Registration Number')
else:
    print('Invalid Vehicle Registration Number')
