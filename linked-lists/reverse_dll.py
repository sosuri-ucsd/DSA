class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_dll(self, head: ListNode) -> ListNode:
    temp = head
    stack = ()
    while temp:
        stack.append(temp)
    temp = head
    while temp:
        e = stack.pop()
        temp.val = e
        temp = temp.next
    return head

def reverse_dll(self, head: ListNode) -> ListNode:
    curr = head
    prev = None
    if curr.next is None:
        
