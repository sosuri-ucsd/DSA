def union(nums1, nums2):
    set12 = set(nums1) | set(nums2)
    return sorted(set12)

def union2(nums1, nums2):
    i, j = 0, 0
    result = []
    
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            if not result or result[-1] != nums1[i]:
                result.append(nums1[i])
            i += 1
        elif nums2[j] < nums1[i]:
            if not result or result[-1] != nums2[j]:
                result.append(nums2[j])
            j += 1
        else:
            if not result or result[-1] != nums1[i]:
                result.append(nums1[i])
            i += 1
            j += 1
    
    while i < len(nums1):
        if result[-1] != nums1[i]:
            result.append(nums1[i])
        i += 1
    
    while j < len(nums2):
        if result[-1] != nums2[j]:
            result.append(nums2[j])
        j += 1
    
    return result