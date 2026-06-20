# You are given an array. The task is to reverse the array and print it.
def reverse_array(lst):
    if lst == []:
        return []
    elif len(lst) == 1:
        return lst
    else:
        return [lst[-1]] + reverse_array(lst[:-1])