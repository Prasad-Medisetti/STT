from re import *
with open('phonenosoutput.txt', 'w') as op:
    with open('phonenos.txt') as ip:
        for line in ip:
            lst = fullmatch('[7-9]\d{9}', line)
            for n in lst:
                op.writeline(n)
    print('Extract successful')
