# Node


class Node:
    def __init__(self, value):
        self.value = value


# linkedlist
class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = Node(value)
        self.next = None
        self.length = 1

    def append(self, value):
        ##its O(n) = 1 as we have the tail referenced

        self.tail.next = Node(value)
        self.tail = Node(value)
        self.length += 1

    def prepend(self, value):
        # no base case as if we construct the linkedlist we get a first node anyway
        self.head.next = self.head  ##wrong! this would create a looop !!!!!
        self.head = Node(value)
        self.length += 1


##correction


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None  ##extremely important: the next attribute is part of the node, not of the linked list, as otherwise we had only one next attribtue instead of several ones (each for each node)


class LinkedList:
    def __init__(self, value):
        new_node = Node(
            value
        )  ##create the node in memory only once! Its memory efficient!
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)  ##same logic to mistake as above

        ## always include edge cases:
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node  ##correct pointer logic
            self.tail = new_node

        self.length += 1

    def prepend(self, value):
        new_node = Node(value)  ##next property is None by default

        # edge case
        if self.length == 0:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head  ##use the next property of the new node
            self.head = new_node

        self.length += 1

    def insert(
        self, index, value
    ):  # insert at location index in LL a node with Value of value, I assume zero indexing
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node

        elif index == 0:
            self.prepend(value)

        # in case we append a node (index is the last one)
        elif index == self.length - 1:
            self.append(value)

        else:
            i = 0
            current_node = (
                self.head
            )  # current_node is a pointer that traverses the list
            # if we have current node, we increment the i by 1, then check if its equals to the index we want
            # and the next to the new one to the old next one
            while current_node:
                i += 1
                if i == index:
                    old_next = current_node.next
                    current_node.next = new_node  # we need to adjust the next of node before (here still the current_node), to point to the new one
                    new_node.next = old_next
                    return  # exit the whie loop if we have inserted it
                current_node = current_node.next

    ##correction for insertion

    def insert(
        self, index, value
    ):  # insert at location index in LL a node with Value of value, I assume zero indexing
        new_node = Node(value)

        ##block below is not needed as its already in the prepend and append method!
        # if self.length == 0:
        #   self.head = new_node
        #  self.tail = new_node

        if index == 0:
            self.prepend(value)
            return  ##always put a return statement to end the loop!!!

        # in case we append a node (index is the last one)
        if (
            index == self.length
        ):  ##corrected the indexing to be correct zero based indexing
            self.append(value)
            return  ##same as above

        else:
            current_node = (
                self.head
            )  # current_node is a pointer that traverses the list
            ##use a for loop instead of a while loop:
            ##start at 1
            for (
                i
            ) in range(  ##we could also have a while loop but would need to adjust the condition: create a current_index = 0 and the condition should be current_index < index-1
                1, index
            ):  ## get to the node before the index where we want to insert it, start at 1 as we are already at node 0 (head node)
                current_node = current_node.next
                if current_node is None:
                    return
            ## now we are at node index-1
            new_node.next = (
                current_node.next
            )  ##using the new_node.next attribute to make things simpler (see pattern below), otherwise it would be redundant i.e. we would use memory for a new variable "old_next"
            current_node.next = new_node
            self.length += 1

    ###next day spaced repetition but this time with while loop
    def insert(self, index, value):
        new_node = Node(value)

        if index < 0 or index > self.length:
            return "Invalid index"

        if index == 0:
            self.prepend(value)
            return

        if (
            index == self.length
        ):  # if we have length of 4 and index takes on 4 in zero indexing, then 4 is the new index to be appended
            self.append(value)
            return

        else:
            current_index = 0
            current_node = self.head

            while current_node is not None and current_index < index - 1:
                current_node = current_node.next
                current_index += 1

            if current_node is None:
                return

            new_node.next = current_node.next
            current_node.next = new_node

        self.length += 1

    def remove(self, index):
        if (
            index < 0 or index >= self.length
        ):  ## >= use the logic of the linked list, its not the same as inserting a node (hence the difference to the one above)
            return "Invalid index"

        if index == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None  ##adjust the tail too!!
            self.length -= 1
            return

        current_index = 0
        current_node = self.head  # I need to reset the current node

        while current_node is not None and current_index < index - 1:
            current_node = current_node.next
            current_index += 1

        if current_node.next is None:
            return

        if current_node.next.next is None:
            current_node.next = (
                None  ##readjust the next node so that it doesnt point to anything else
            )
            self.tail = current_node

        else:  # we have a next node and a next node after that
            current_node.next = current_node.next.next
            ##self.tail = current_node.next.next not needed as its already the tail

        self.length -= 1

    def reverse(self):  # per init we have a LL with at least 1 node
        # edge case: we just have one node
        if self.length == 1:
            return "LL reversed"

        # normal case: we have at least two nodes
        current_node = (
            self.head
        )  # points to the first node in the list that should be the last
        current_index = 0

        # set framework for traversing the LL
        while (
            current_node is not None and current_index < self.length - 1
        ):  # if we have 4 nodes, self.length is 4 but the index of the fourth node is 3 (zero based indexing)
            old_prev = current_node  # this again points to the node 1 in memory,
            old_next = current_node.next  # points to node 2 in memory,

            # edge case within normal cases
            if current_index == 0:
                old_prev.next == None
                self.tail = current_node

            current_node = old_next
            current_index += 1
            # go to old
        # we exit the loop at index 3 when node has 4 nodes and the last is indexed at node 3
        self.head = old_prev
        return "LL reversed"

    ##correction
    def reverse_corr(self):  # per init we have a LL with at least 1 node
        # edge case: we just have one node
        if self.length == 1:
            return "LL reversed"

        # normal case: we have at least two nodes
        current_node = (
            self.head
        )  # points to the first node in the list that should be the last
        ## not needed -> current_index = 0 as I want to traverse through the entire list and not get a certain point in between like in the inser

        ##set the other two pointers
        previous_node = None
        old_next_node = None  ##acts as a temporary variable

        # set framework for traversing the LL
        while (
            current_node is not None
        ):  ## and current_index < self.length-1: -> not needed as I want to traverse the entire ll (just as above)
            ##old_next = current_node.next #points to node 2 in memory,
            old_next_node = current_node.next

            # reset the next attribute of node 1 (head node)
            current_node.next = previous_node
            # set previous node pointer to the current node 1 before we traverse to next node 2 in old direction
            previous_node = current_node
            # traverse the list in the old direction from left to right i.e. to node 2
            current_node = old_next_node

        # trick: once we done we just reset the self.head to self.tail, save a temp variable and self.tail to temp
        temp = self.head
        self.head = self.tail
        self.tail = temp
        return "LL reversed"

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value, end=" -> ")
            current_node = current_node.next
        print("None")
        print(f"head of LL {self.head.value}")
        print(f"tail of LL {self.tail.value}")


"""pattern reversing a ll: 3 pointers: one for traversing the list called current_node, one for the previous_node and one for the old_next_node"""


"""Pattern:
When working with linked lists, it's often more straightforward and less error-prone to manipulate the 
next attribute of individual Node objects rather than trying to directly manipulate the next attributes of nodes through the LinkedList class's 
attributes like self.head.
Each Node is responsible for knowing its own value and the next node in the sequence. The LinkedList class is responsible for higher-level operations 
that involve multiple nodes, like adding or removing nodes, but it delegates the responsibility of knowing the 'next' node to the individual Node objects."""

ll = LinkedList(4)

ll.append(5)

ll.append(6)

# print(ll.head.value)
# print(ll.tail.value)


ll.print_list()

ll.reverse_corr()

ll.print_list()

# print(ll.head.value)
# print(ll.tail.value)
