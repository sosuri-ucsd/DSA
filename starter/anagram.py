def anagram(s1,s2):
    list1 = list(iter(s1))
    list2 = list(iter(s2))
    list1.sort()
    list2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if list1[pos] == list2[pos]:
            pos = pos + 1
        else:
            matches = False

    return matches
