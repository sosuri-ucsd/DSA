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