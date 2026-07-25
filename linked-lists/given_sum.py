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



