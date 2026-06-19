# Brute Force Solution
def gcd(a, b):
    gcd = 1
    for i in range(1, min(a,b) + 1):
        if a % i == 0 and b % i == 0:
            gcd = i
    return gcd

# Optimal 
def gcd(x, y):
    while x > 0 and y > 0:
        if x > y:
            x = x % y
        else:
            y = y % x
    if x == 0:
        return y
    return x

    

