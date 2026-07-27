def remove_duplicates(self, head):
    if head is None:
        return head
    curr = head
    while curr and curr.next:
        if curr.val == curr.next.val:
            dup = curr.next
            curr.next = dup.next
            if dup.next:
                dup.next.prev = curr
        curr = curr.next
    return head 


