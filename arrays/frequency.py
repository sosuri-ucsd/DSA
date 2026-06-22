# Count frequency of each element in the array
def frequency(arr):
    dct = {}
    for elem in arr:
        if elem not in dct:
            dct[elem] = 1
        else:
            dct[elem] += 1
    for elem in dct:
        print (elem, dct[elem])
    