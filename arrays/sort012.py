def sort_arr(nums):
        cnt0 = 0
        cnt1 = 0
        cnt2 = 0
        for num in nums:
            if num == 0:
                cnt0 += 1
            elif num == 1:
                cnt1 += 1
            else:
                cnt2 += 1
        for i in range(cnt0):
            nums[i] = 0
        for j in range(cnt0, cnt0 + cnt1):
            nums[j] = 1
        for k in range(cnt0 + cnt1, cnt0 + cnt1 + cnt2):
            nums[k] = 2