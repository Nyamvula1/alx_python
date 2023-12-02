def fibonacci_sequence(n):
    n=int(input())
    if n <= 1:
        return n
    else:
        return fibonacci_sequence(n-1) + fibonacci_sequence(n-2)

