def merge(lst, low, mid, high):
    temp = []
    left, right = low, mid + 1
    while left <= mid and right <= high:
        if lst[left] <= lst[right]:
            temp.append(lst[left])
            left += 1
        else:
            temp.append(lst[right])
            right += 1
    while left <= mid:
        temp.append(lst[left])
        left += 1
    while right <= high:
        temp.append(lst[right])
        right += 1
    for i in range(low, high + 1):
        lst[i] = temp[i - low]
    
def merge_sort(arr, low, high):
    if low >= high:
        return
    mid = (low + high) // 2
    merge_sort(arr, low, mid)
    merge_sort(arr, mid + 1, high)
    merge(arr, low, mid, high)



    