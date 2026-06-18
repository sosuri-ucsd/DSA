# Checks if an integer/number is a palindrome
def palindrome(s):
    str_version = str(s)
    return str_version == str_version[::-1]