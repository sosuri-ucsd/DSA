def first_and_last_occurence(arr, target):
    lst = []
    if not lst:
        return [-1, -1]
    for i in range(len(arr)):
        if arr[i] == target:
            lst.append(i)
    return [lst[0], lst[-1]]

def first_and_last_occurence(arr, target):
    low = 0 
    high = len(arr) - 1
    lb = len(arr)
    ub = len(arr)
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] >= target:
            lb = mid
            high = mid - 1
        else:
            low = mid + 1
    
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] > target:
            ub = mid
            high = mid - 1
        else:
            low = mid + 1
        
    return [lb, ub]