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


def two_sum(nums, target):
     hm = {}
     for i, num in enumerate(nums):
          complement = target - num
          if complement in hm:
               return [hm[complement], i]
          else:
               hm[num] = i
     return [-1, -1]


def two_sum(arr, target):
     for i in range(0, len(arr) - 1):
          for j in range(i + 1, len(arr)):
               if arr[i] + arr[j] == target:
                    return [i, j]
     return [-1, -1]