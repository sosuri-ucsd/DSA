def maximum_subarray_sum(arr):
    maxi = float('-inf')
    for i in range(len(arr)):
        total = 0
        for j in range(i, len(arr)):
            total += arr[j]
            maxi = max(maxi, total)
    return maxi
