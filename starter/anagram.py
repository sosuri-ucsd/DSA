# Checks if two strings are anagrams
def anagram(s1,s2):
    return sorted(list(iter(s1))) == sorted(list(iter(s2)))
