def fib(n):
    f = [0,1]
    while len(f)<=n:
        f.append(f[-1]+f[-2])
    return f
n = int(input())
print(*fib(n))
