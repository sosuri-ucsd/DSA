def selection(lst):
    for i in range(len(lst)-1):
        minpos = i
        for j in range(i, len(lst)):
            if lst[j] < lst[minpos]:
                minpos = j
        
        temp = lst[i]
        lst[i] = lst[minpos]
        lst[minpos] = temp
        
    return lst
