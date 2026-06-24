def singleNumber(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for num in nums:
            result ^= num
        return result


# Brute hashmap way
def singleNumber(nums):
    hm = {}
    for element in nums:
        if element not in hm:
            hm[element] = 1
        else:
            hm[element] += 1
        
    for element in hm:
        if hm[element] == 1:
            return element

