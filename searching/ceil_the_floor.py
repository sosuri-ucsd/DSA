def floo_and_ceil(arr, target):
    floor, ceil = -1, -1
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return [arr[mid], arr[mid]]
        elif arr[mid] > target:
            ceil = arr[mid]
            high = mid - 1
        else:
            floor = arr[mid]
            low = mid + 1
    return [floor, ceil]
