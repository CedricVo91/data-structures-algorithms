class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.bottom = None
        self.top = None
        self.length = 0

    def peek(self):  # give me the top of the stack
        return self.top

    def push(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.bottom = new_node
            self.top = new_node
            self.lenght += 1
            return

        old_top = self.top
        self.top = new_node
        ## big confusion was: in a stack the top points to the one below if we implement the stacl using a linked list...
        self.top.next = old_top
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None

        old_top = self.top
        self.top = self.top.next
        self.length -= 1
        return old_top
