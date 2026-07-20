def first_and_last_occurence(arr, target):
    lst = []
    for i in range(len(arr)):
        if arr[i] == target:
            lst.append(i)
    if not lst:
        return [-1, -1]
    return [lst[0], lst[-1]]

def first_and_last_occurrence(arr, target):
    def lower_bound():
        lb = len(arr)
        low, high = 0, len(arr)-1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] >= target:
                lb = mid
                high = mid - 1
            else:
                low = mid + 1
        return lb

    def upper_bound():
        ub = len(arr)
        low, high = 0, len(arr)-1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] > target:
                ub = mid
                high = mid - 1
            else:
                low = mid + 1
        return ub

    lb = lower_bound()
    ub = upper_bound()
    if lb == len(arr) or arr[lb] != target:
        return [-1, -1]
    return [lb, ub - 1]