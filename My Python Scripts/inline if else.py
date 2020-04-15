# inline if else
l = list(range(1,11))

[print(x, ': Even') if x%2==0 else print(x, ': Odd') for x in l]