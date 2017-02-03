#Define a faster fibonacci procedure that will enable us to computer
#fibonacci(36).

def fibonacci(n):
    i = 0
    fib = 0
    prev1 = 0
    prev2 = 0
    while i < n + 2:
        if i == 0:
            prev1 = 0
        elif i == 1:
            prev2 = 1
        else:
            fib = prev1 + prev2
            if i % 2 > 0:
                prev1 = fib
            else:
                prev2 = fib
        i += 1
    return fib



print fibonacci(10)

print fibonacci(36)
#>>> 14930352
