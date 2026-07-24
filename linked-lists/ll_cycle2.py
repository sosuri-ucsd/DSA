# Return start of the cycle - BRUTE(O(N), O(N))
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def linkedlist_cycle2(self, head: ListNode) -> ListNode:
    temp = head
    my_set = set()
    while temp is not None:
        if temp in my_set:
            return temp
        my_set.add(temp)
        temp = temp.next
    return "Not Found"
        

# OPTIMAL 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def linkedlist_cycle2(self, head: ListNode) -> ListNode:
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
    return None
