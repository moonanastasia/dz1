def f(n):
    factorial = 1
    while n > 0:
        factorial *= n
        n -= 1
    return factorial

print(f(7))