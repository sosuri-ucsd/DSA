# Re arrange elements by sign
def rearrange(arr):
    pos = []
    neg = []
    nums = []
    for elem in arr:
        if elem >= 0:
            pos.append(elem)
        else:
            neg.append(elem)
    
    for i in range(len(pos)):
        nums.append(pos[i])
        nums.append(neg[i])

    return nums


def rerrange2(arr):
    result = [0] * len(arr)
    pos = 0
    neg = 1
    for i in range(len(arr)):
        if arr[i] >= 0:
            result[pos] = arr[i]
            pos += 2
        else:
            result[neg] = arr[i]
            neg += 2
    return result