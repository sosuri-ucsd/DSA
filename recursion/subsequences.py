def solve(ind, subset):
    result = []
    if ind >= len(nums):
        result.append(subset.copy())
        return
    subset.append(nums[ind])
    solve(ind + 1, subset)
    subset.pop()
    solve(ind + 1, subset)