def missing_number(nums): # BRUTE
    n = len(nums)
    for i in range(n):
        if i not in nums:
            return i
        
def missing_number(arr): # BETTER
    n = len(arr)
    freq = {}
    for i in range(n):
        freq[i] = 0
    for num in arr:
        if num in freq:
            freq[num] = 1
    for k, v in freq.items():
        if v == 0:
            return k

def missing_number(lst): # OPTIMAL
    n = len(lst)
    sum_lst = sum(lst)
    sum = ((n) * (n + 1)) // 2
    return sum - sum_lst

