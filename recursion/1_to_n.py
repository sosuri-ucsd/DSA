# Given an integer n, write a program to print numbers from 1 to n.
def one_to_n(n):
    if n == 0:
        return
    else:
        one_to_n(n-1)
    print(n)

# Given an integer N, write a program to print numbers from N to 1.
def one_to_n(n):
    if n == 0:
        return
    else:
        print(n)
    one_to_n(n-1)
