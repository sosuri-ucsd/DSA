# Longest consecutive sequence in an array
def longest_sequence(nums):
    max_count = 0
    for i in range(len(nums)):
        num = nums[i]
        count = 1
        while (num+1) in nums:
            count += 1
            num += 1
        max_count = max(max_count, count)
    return max_count

def longest_sequence2(nums):
    nums.sort()
    count = 0
    last_smaller = float('-inf')
    longest = 0
    for i in range(len(nums)):
        num = nums[i]
        if num - 1 == last_smaller:
            count += 1
            last_smaller = num
        elif num != last_smaller:
            count = 1
            last_smaller = num
        longest = max(longest, count)
    return longest  