class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value):
        self.first = None
        self.last = None
        self.length = 0

    def peak(self):
        return self.first

    def enqueue(self, value):
        new_node = Node(value)
        self.last.next = new_node
        self.last = new_node

    def dequeue(self, value):
        holding_pointer = self.first
        self.first = self.first.next
        return holding_pointer
