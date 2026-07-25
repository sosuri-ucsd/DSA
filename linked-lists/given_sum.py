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

def pairs_given_sum(self, head, target):
    result = []
    right = head
    while right.next:
        right = right.next
    left = head
    while left is not None and right is not None and left.val < right.val:
        if left.val + right.val == target:
            result.append([left.val, right.val])
            left = left.next
            right = right.prev
        elif left.val + right.val > target:
            right = right.prev
        else:
            left = left.next 
    return result








