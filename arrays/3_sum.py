# BRUTE FORCE
def three_sum(arr):
    my_set = set()
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            for k in range(j+1, len(arr)):
                if arr[i] + arr[j] + arr[k] == 0:
                    temp = [arr[i], arr[j], arr[k]]
                    temp.sort()
                    my_set.add(tuple(temp))

    return [list(ans) for ans in my_set]

# BETTER
def three_sum(arr):
    result = set()
    for i in range(len(arr)):
        my_set = set()
        for j in range(i+1, len(arr)):
            third = -(arr[i] + arr[j])
            if third in my_set:
                temp = [arr[i], arr[j], third]
                temp.sort()
                result.add(tuple(temp))
            my_set.add(arr[j])
    return [list(ans) for ans in result]

# OPTIMAL
def three_sum(arr):
    ans = []
    n = len(arr)
    arr.sort()
    for i in range(n):
        if i != 0 and arr[i] == arr[i-1]:
            continue
        j = i + 1
        k = n - 1
        while j < k:
            total_sum = arr[i] + arr[j] + arr[k]
            if total_sum < 0:
                j += 1
            elif total_sum > 0:
                k -= 1
            else:
                temp = [arr[i], arr[j], arr[k]]
                ans.append(temp)
                j += 1
                k -= 1
                while j < k and arr[j] == arr[j-1]:
                    j += 1
                while j < k and arr[k] == arr[k+1]:
                    k -= 1
    return ans
    