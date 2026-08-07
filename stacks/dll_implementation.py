# Implementation using DLL
class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class Stack: # Stack
    def __init__(self):
        self.head = None

    def push(self, val):
        new_node = Node(val)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def pop(self):
        if self.head is None:
            return "Stack is empty"
        val = self.head.val
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        return val

    def peek(self):
        return self.head.val if self.head else "Stack is empty :("


class Queue: # Queue
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, val):
        new_node = Node(val)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def dequeue(self):
        if self.head is None:
            return "Queue is empty"
        val = self.head.val
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        return val

    def peek(self):
        return self.head.val if self.head else "Queue is empty"