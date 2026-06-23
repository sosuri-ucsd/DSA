# Given an array, find the second smallest and second largest element in the array. Print ‘-1’ in the event that either of them doesn’t exist.
def second_largest_smallest(arr):
    if len(arr) <= 1:
        return (-1, -1)
    
    small = float('inf')
    second_small = float('inf')
    large = float('-inf')
    second_large = float('-inf')
    for i in arr:
        small = min(small, arr[i])
        large = max(large, arr[i])
    
    for i in range(n):
        if arr[i] < second_small and arr[i] != small:
            second_small = arr[i]
        if arr[i] > second_large and arr[i] != large:
            second_large = arr[i] 
    
    print("Second smallest is", second_small)
    print("Second largest is", second_large)

    
    