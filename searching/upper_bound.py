def upper_bound(arr, target):
    low = 0 
    high = len(arr) - 1
    ub = len(arr)
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > target:
            ub = mid
            high = mid - 1
        else:
            low = mid + 1
    return ub
