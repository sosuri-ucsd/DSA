def linkedlist_cycle2(self, head):
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



def linkedlist_cycle2(self, head):
    if head == None or head.next is None:
        return head
    odd = head
    even = head.next
    even_head = even
    while even is not None and even.next is not None:
         odd.next = odd.next.next
         odd = odd.next
         even.next = even.next.next
         even = even.next
    odd.next = even_head
    return head
