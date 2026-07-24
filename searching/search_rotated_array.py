def search_rotated_sorted_array(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid 
        if arr[mid] <= arr[high]:
            if arr[mid] <= target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
        else:
            if arr[low] <= target <= arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
    return -1