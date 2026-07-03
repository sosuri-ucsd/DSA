# Given an array, find the second smallest and second largest element in the array. Print ‘-1’ in the event that either of them doesn’t exist.
def second_largest_smallest(arr):
    if len(arr) <= 1:
        return (-1, -1)
    
    largest, second_largest = float('-inf'), float('-inf')
    smallest, second_smallest = float('inf'), float('inf')
    
    for elem in arr:
        # update largest and second largest
        if elem > largest:
            second_largest = largest
            largest = elem
        elif elem > second_largest and elem != largest:
            second_largest = elem
        
        # update smallest and second smallest
        if elem < smallest:
            second_smallest = smallest
            smallest = elem
        elif elem < second_smallest and elem != smallest:
            second_smallest = elem
    
    if second_largest == float('-inf') or second_smallest == float('inf'):
        return (-1, -1)
    
    return (second_smallest, second_largest)
    






def second_largest(arr):
    largest = float('-inf')
    sec = float('-inf')
    for i in range(len(arr)):
        if arr[i] > largest:
            sec = largest
            largest = arr[i]
        elif arr[i] > sec and arr[i] < largest:
            sec = arr[i]
    return sec