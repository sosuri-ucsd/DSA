def lower_bound(arr, target):
    lb = len(arr)
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= target:
            lb = mid
            high = mid - 1
        else:
            low = mid + 1
    return lb
