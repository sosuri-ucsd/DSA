# Count frequency of each element in the array
def frequency(arr):
    dct = {}

    for elem in arr:
        if elem not in dct:
            dct[elem] = 1
        else:
            dct[elem] += 1

    high_elem = arr[0]
    low_elem = arr[0]
        
    for elem in dct:
            if dct[elem] > dct[high_elem]:
                high_elem = elem
            if dct[elem] < dct[low_elem]:
                low_elem = elem
        
    return high_elem, low_elem