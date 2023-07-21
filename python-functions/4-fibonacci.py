def fibonacci_sequence(n):
    fib = []
    for i in range(n):
        if i <= 1:
            fib.append(i)
        else:
            fib.append(fib[-1] + fib[-2])
    return fib