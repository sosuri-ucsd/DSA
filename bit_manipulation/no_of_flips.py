def no_of_flips(a, b):
    ans = a ^ b
    count = 0
    for i in range(32):
        if ans & (1 << i) == 0:
            count += 1
    return count
