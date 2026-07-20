# OPTIMAL
def search_insert_pos(arr, target):
    low = 0 
    high = len(arr) - 1
    lb = len(arr)
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] >= target:
            lb = mid
            high = mid - 1
        else:
            low = mid + 1
    return lb