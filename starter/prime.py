# Checks if a number is a prime number (Brute)
def prime(x):
    lst = []
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            lst.append(i)
            if i != x//i:
                lst.append(x//i)
    if len(lst) > 2:
        return False
    else:
        return True