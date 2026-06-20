# Problem Statement: Given an integer N. Print the Fibonacci series up to the Nth term.
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_series(n):
    for i in range(n+1):
        print(fibonacci(i), end=' ')



# Better solution
def fibonacci(n):
    if n == 0:
        print(f"The Fibonacci Series up to {n}th term:")
        print(0)
    else:
        second_last = 0
        last = 1
        print(f"The Fibonacci Series up to {n}th term:")
        print(f"{second_last} {last}", end=" ")

        for i in range(2, n + 1):
            cur = last + second_last
            second_last = last
            last = cur
            print(cur, end=" ")