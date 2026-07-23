class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    def append(self, val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node
    def traversal(self):
        if self.head == None:
            print("SLL is empty")
        else:
            curr = self.head
            while curr is not None:
                print(curr.val, end = " ")
                curr = curr.next
            print()
    def insert(self, position, val):
        new_node = Node(val)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            curr = self.head
            prev = None
            count = 0
            while curr is not None and count < position:
                prev = curr
                curr = curr.next
                count += 1
            prev.next = new_node
            new_node.next = curr
    def delete(self, val):
        temp = self.head
        if temp.next is not None:
            if temp.val == val:
                self.head = temp.next
                return 
            else:
                found = False
                prev = None
                while temp is not None:
                    if temp.val == val:
                        found = True
                        break
                    prev = temp
                    temp = temp.next
            if found:
                prev.next = temp.next
                return 
            else:
                print("Node not found")

node1 = Node(5)
node2 = Node(10)
node3 = Node(7)
node4 = Node(8)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = None
 
print(node1.val)
print(node1.next.val)
print(node2) # Same as line above



def delete(self, val):
    if self.head is None:
        print("Not Found")
        return
    if self.head.val == val:
        self.head = self.head.next
        return
    
    prev = None
    curr = self.head
    while curr is not None:
        if curr.val == val:
            prev.next = curr.next
            return
        prev = curr
        curr = curr.next

    print("Not Found")




