def min_rotated_sorted_array(arr):
    min = float('inf')
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] <= arr[high]:
            mini = min(mini, arr[mid])
            high = mid - 1
        else:
            mini = min(mini, arr[low])
            low = mid + 1
    return mini
 

