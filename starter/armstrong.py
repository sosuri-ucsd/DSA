def armstrong(x):
    # Step 1: count number of digits
    count = len(str(x))
    # Step 2: Find the sum
    original = x
    sum = 0
    while x > 0:
        last = x % 10
        sum += last ** count
        x //= 10
    # Step 3: Compare
    return sum == original
