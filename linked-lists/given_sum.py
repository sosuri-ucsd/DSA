def pairs_given_sum(self, head, target):
    temp1 = head
    result = []
    while temp1:
        temp2 = temp1.next
        while temp2:
            if temp1.val + temp2.val == target:
                result.append([temp1.val, temp2.val])
            temp2 = temp2.next
        temp1 = temp1.next
    return result

def pairs_given_sum(self, head, target):
    my_set = set()
    temp = head
    result = []
    while temp is not None:
        remaining = target - temp.val
        if remaining in my_set:
            result.append([remaining, temp.val])
        my_set.add(temp.val)
        temp = temp.next
    return result



