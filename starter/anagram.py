# Checks if two strings are anagrams (O(n logn))
def anagram(s1,s2):
    return sorted(list(iter(s1))) == sorted(list(iter(s2)))

# O(n) + easiest solution if we are allowed to import 
from collections import Counter
def anagram(s1, s2):
    return Counter(s1) == Counter (s2)

# Time - O(n), Space - O(1)
def anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    count = {}
    for char in s1:
        count[char] = count.get(char, 0) + 1
    for char in s2:
        count[char] = count.get(char, 0) - 1
    return all(v == 0 for v in count.values())


# Time - O(n), Space - O(1)
def anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    counter1 = {}
    counter2 = {}
    for element in list(s1):
        if element in counter1:
            counter1[element] += 1
        else:
            counter1[element] = 1
    for element2 in list(s2):
        if element2 in counter2:
            counter2[element2] += 1
        else:
            counter2[element2] = 1
    if counter1 == counter2:
        return True
    else:
        return False

