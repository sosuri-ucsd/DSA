# Find the highest/lowest frequency element
def high_and_low(arr):
    dct = {}
    for elem in arr:
        if elem not in dct:
            dct[elem] = 1
        else:
            dct[elem] += 1
    
    for element in dct:
        max_arr = dct[element]
        min_arr = dct[element]
        

        
    
