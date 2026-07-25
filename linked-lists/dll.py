class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class dll:
    def __init__(self):
        self.head = None
    def insert_at_head(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    def append(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current
    def insert_in_between(self, val, position):
        new_node = Node(val)
        if position == 0:
            if not self.head:
                self.head = new_node
            else:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            return


        current = self.head
        count = 0
        while current and count < position - 1:
            current = current.next
            count += 1
        if current is None:
            print("Position out of bounds")
            return
        new_node.next = current.next
        new_node.prev = current
        if current.next:
            current.next.prev = new_node
        current.next = new_node

    def traverse(self, head):
        curr = self.head
        while curr:
            print(curr.val)
            curr = curr.next

    def delete_head(self, head):
        if self.head is None:
            return "Not Found"
        if self.head.next is None:
            self.head = None
            return
        else:
            self.head = self.head.next
            self.head.prev = None

    def delete_last(self, head):
        if self.head is None:
            return "Not Found"
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def delete_at_position(self, position):
        if self.head is None:
            return "Not Found"

        if position == 0:
            if self.head.next is None:
                self.head = None
                return
            next_node = self.head.next
            next_node.prev = None
            self.head = next_node
            return

        current = self.head
        count = 0
        while current and count < position:
            current = current.next
            count += 1

        if current is None:
            print("Position out of bounds")
            return

        prev_node = current.prev
        next_node = current.next

        if prev_node:
            prev_node.next = next_node
        if next_node:
            next_node.prev = prev_node
                




    



        


