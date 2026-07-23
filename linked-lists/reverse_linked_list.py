# Pre-defined Node class (you don't write this)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(self, head: ListNode) -> ListNode:
    temp = head
    stack = []
    while temp is not None:
        stack.append(temp.val)
        temp = temp.next
    temp = head
    while temp is not None:
        e = stack.pop()
        temp.val = e
        temp = temp.next
    return head

