def remove_keyl(head, key):
    if head.next is None and head.val == key:
        return None
    temp = head
    prev = None
    new_head = head
    while temp:
        if temp.val == key:
            if prev is not None:
                prev.next = temp.next
            if temp.next is not None:
                temp.next.prev = prev
            if temp == new_head:
                new_head = new_head.next
        prev = temp
        temp = temp.next
    return new_head


