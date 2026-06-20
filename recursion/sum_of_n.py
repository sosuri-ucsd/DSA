# Given a number ‘N’, find out the sum of the first N natural numbers .
def sum(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n + sum(n-1)