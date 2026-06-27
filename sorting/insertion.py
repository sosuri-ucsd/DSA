# Insertion Sort
def insertion(lst):
    for i in range(1, len(lst)):
        j = i
        while lst[j-1] > lst[j] and j > 0:
            lst[j-1], lst[j] = lst[j], lst[j-1]
            j -=1
    return lst

