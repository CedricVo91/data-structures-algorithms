class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def __repr__(self):
        return str([v for v in self])

    def reverse(
        linked_list,
    ):  # idea is to create a function that is not dependant of a specific object "linkedlist"
        # important to test: here we enter a linkedlist object and we should not use self. self only if we use the linkedlist of itself -> research the difference between reverse(ll) and ll.reverse()

        # edge case: empty linked list
        if linked_list.head is None:
            return

        # edge case linkedlist is
        if linked_list.head.next is None:
            return linked_list

        # traverse the node of the linked list and turn the pointer 180 degrees around (each node points in the opposite direction)

        current_node = linked_list.head
        previous_node = None  # we set this to none for first node, so the initial direction is not the old one towards node 2
        while current_node is not None:
            # Store the next node before we alter current_node's next pointer
            old_current_node = current_node

            current_node.next = previous_node
            previous_node = current_node
            # assign new current to the next node of the old version of the current node
            current_node = old_current_node.next

        # set the head to the last node by assigning it to the correct current node which we saved in previous node
        linked_list.head = previous_node
        return linked_list
        # the new current node is the next one
        # we want the next pointer of the current node to point to previous node
        # with current_node.next, we only change the pointer of current node selected, not the whole list structure
        # think about it in terms of each object and its attributes

    # problem above: its a loop thats never ending... the current node.next is pointing to the previous node
    # this problem is about assigning the variables correctly and in correct order
    # one has to go to old direction, and one variable has to point to previous as next
    # change the header to point in the last iteration of nodedef reverse(linked_list): #idea is to create a function that is not dependant of a specific object "linkedlist"
    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out


llist = LinkedList()
llist2 = LinkedList()
for value in [4, 2, 5, 1, -3, 0]:
    llist.append(value)

flipped = llist2.reverse()

listx = [
    1,
    2,
    3,
    4,
]  # creates a new object in memory: a list containing of immutable objects "int"

import copy

listx2 = copy.deepcopy(listx[:2])

print(listx)
print(listx2)
