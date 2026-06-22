# Given a number X,  print its factorial.
def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)
