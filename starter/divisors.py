def divisors(x):
    empty = []
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            empty.append(i)
            if i != x // i:
                empty.append(x // i)
    return empty
