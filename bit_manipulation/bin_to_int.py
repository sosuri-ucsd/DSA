def bin_to_int(x):
    decimal_number = 0
    pow = 0
    for i in x[::-1]:
        decimal_number += int(i) * 2 ** pow
        pow += 1
    return decimal_number
