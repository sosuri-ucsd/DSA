# Selection sort
def selection(lst):
    for i in range(len(lst)-1):
        minpos = i
        for j in range(i, len(lst)):
            if lst[j] < lst[minpos]:
                minpos = j
        
        lst[i], lst[minpos] = lst[minpos], lst[i]
    return lst
