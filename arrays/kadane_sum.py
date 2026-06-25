def kadane_array(arr):
    maxi = float('-inf')
    sum = 0
    start = 0
    ansStart = 0
    ansend = 0
    for i in range(len(arr)):
        if sum == 0:
            start = i
        sum += arr[i]

        if sum > maxi:
            maxi = sum
            ansStart = start
            ansend = i
        if sum < 0:
            sum = 0
        
    return arr[ansStart: ansend + 1]
        

