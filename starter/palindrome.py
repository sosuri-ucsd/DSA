# Checks if an integer/number is a palindrome
def palindrome(s):
    str_version = str(s)
    return str_version == str_version[::-1]

# Optimal Solution with O(log n):
def palindrome(x):
    newnum = 0
    duplicate = x
    while x > 0:
        last = x % 10
        newnum = newnum * 10 + last
        x = x // 10
    return newnum == duplicate

