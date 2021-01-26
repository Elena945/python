from math import factorial
    from itertools import count

def fibo_gen(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
        yield factorial(f)


n = int(input("factorial number\n"))
for _ in fibo_gen(n):
    print(_)





