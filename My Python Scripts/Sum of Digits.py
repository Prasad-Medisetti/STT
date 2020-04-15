#n = int(input("Enter an integer: "))
#s = 0
#while n > 0:
#    s += n%10
#    n //= 10
#print(s)

# Another Way

n = input("Enter an integer: ")
print(sum([int(x) for x in n]))