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


def longest_sequence3(arr):
    my_set = set()
    for i in arr:
        my_set.add(i)

    longest = 0
    count = 0
    
    for num in my_set:
        if num - 1 not in my_set:
            x = num
            count = 1
            while x + 1 in my_set:
                count += 1
                x += 1
            longest = max(longest, count)
    return longest


