# Two Sum      
def two_sum(nums, target):
        hm = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hm:
                return [hm[complement], i]
            else:
                hm[num] = i
        return [-1, -1]
