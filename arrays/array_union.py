def union(nums1, nums2):
    set12 = set(nums1) | set(nums2)
    return sorted(set12)

def union2(nums1, nums2):
    n = len(nums1)
    m = len(nums2)
    i, j = 0, 0
    result = []

    while i < n and j < m:
        if nums1[i] <= nums2[j]:
            if result == [] or result[-1] != nums1[i]:
                result.append(nums1[i])
            i += 1
        else:
            if result == [] or result[-1] != nums2[j]:
                result.append(nums2[j])
            j += 1
    
    while i < n:
        if result == [] or result[-1] != nums1[i]:
                result.append(nums1[i])
        i += 1

    while j < m:
        if result == [] or result[-1] != nums2[j]:
                result.append(nums2[j])
        j += 1
    
    return result

