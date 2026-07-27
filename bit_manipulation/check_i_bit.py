def check_ith_bit(n, i):
    return (n >> i) & 1 == 1

def check_ith_bit(n, i):
    return n & (1 << i) == 1