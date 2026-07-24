class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def linkedlist_cycle2(self, head: ListNode) -> ListNode:
    temp = head
    travel = 0
    my_dict = dict()
    while temp is not None:
        if temp in my_dict:
            return travel - my_dict[temp]
        my_dict[temp] = travel
        travel += 1
        temp = temp.next
    return 0


def linkedlist_cycle2(self, head: ListNode) -> ListNode:
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = slow.next
            count = 1
            while slow != fast:
                slow = slow.next
                count += 1
            return count
    return 0

