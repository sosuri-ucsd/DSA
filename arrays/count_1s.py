# Give an array that contains only 1 and   the count of maximum consecutive ones in the array.
def count_consective_ones(nums):
    count = 0
    maxi = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
        else:
            count = 0
        maxi = max(maxi, count)
    return maxi
