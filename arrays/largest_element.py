# Given an array, we have to find the largest element in the array.
def largest_element(arr):
    max_arr = arr[0]
    for elem in arr:
        if elem > max_arr:
            max_arr = elem
    return max_arr