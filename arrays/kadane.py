def kadane(nums):
        maxi = float('-inf')
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum > maxi:
                maxi = sum
            if sum < 0:
                sum = 0
        return maxim