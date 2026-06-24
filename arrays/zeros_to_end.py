# Move all zeroes to the end

def zero_to_end(nums):
    j = 0
    for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
    for a in range(j, len(nums)):
            nums[a] = 0