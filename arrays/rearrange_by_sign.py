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
