# BRUTE
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def linkedlist_cycle(self, head: ListNode) -> ListNode:
    temp = head
    my_set = set()
    while temp is not None:
        if temp in my_set:
            return True
        my_set.add(temp)
        temp = temp.next
    return False