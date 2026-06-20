# Problem Statement: Given a string, check if the string is palindrome or not. A string is said to be palindrome if the reverse of the string is the same as the string.
def palindrome(s):
    if s == '':
        return ''
    elif len(s) == 1:
        return True
    else:
        return (s[0] == s[-1]) and palindrome(s[1:-1])