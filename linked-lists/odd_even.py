def linkedlist_cycle2(self, head: ListNode) -> ListNode:
    temp = head
    values = []
    if head == None or head.next is None:
        return head
    while temp and temp.next:
         values.append(temp.val)
         temp = temp.next.next
    temp = head.next
    while temp and temp.next:
             values.append(temp.val)
             temp = temp.next.next
    index = 0
    temp = head
    while temp is not None:
          temp.val = values[index]
          index += 1
          temp = temp.next
    return head

