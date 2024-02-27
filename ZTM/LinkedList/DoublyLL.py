class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DLL:
    def __init__(self, value):
        entry_node = Node(value)
        self.head = entry_node
        self.tail = entry_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.length += 1

    def prepend(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node

        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

        self.length += 1

    def insert(self, index, value):
        new_node = Node(value)

        if index < 0 or index > self.length:
            return "index out of range: invalid index"

        if index == 0:
            self.prepend(value)
            return

        if (
            index == self.length
        ):  # zero indexing means that if we have self.length of 4, the index will be 0,1,2,3. Hence an index == self.length will append that node in that 4th index
            self.append(value)
            return

        # normal case: we need to traverse the list
        # initialize traversing counter index
        current_index = 0
        # initialize the first node to current_node pointer
        current_node = self.head

        # if index = 2, we want to insert a node after 0,1 -> 2. Hence the third position in our DLL and need to stop at index - 1 i.e. node 1
        while current_index < index - 1 and current_node is not None:
            current_node = current_node.next
            current_index += 1

        ##this should be not needed in a correctly DLL implementation. However, it serves as a safeguard against more difficult implementations
        if current_node is None:
            return

        # we are at current_node with current_index =  index -1
        # reset current_node.next
        # test if node after the one we insert exists
        new_node.next = current_node.next
        if current_node.next is not None:
            current_node.next.prev = new_node

        # if node.next after the one we insert is none i.e. does not exist i.e. we append a node
        # reset current node
        current_node.next = new_node
        new_node.prev = current_node

        self.length += 1

    def remove(self, index):  ## no need for value parameter in a remove function!!
        if (
            index < 0 or index >= self.length
        ):  # index must be equals or bigger only in the remove function,
            return "index out of range: invalid index"

        if index == 0:
            self.head = self.head.next
            # check if DLL becomes empty i.e. we only had one node
            if self.head is None:
                self.tail = None
            ###not empty-> readjust the prev of the new self.head to point to nothing i.e. None
            else:
                self.head.prev = None

            self.length -= 1
            return   

        # initialize traversing counter index
        current_index = 0
        # initialize the first node to current_node pointer
        current_node = self.head

        # if index = 2, we want to insert a node after 0,1 -> 2. Hence the third position in our DLL and need to stop at index - 1 i.e. node 1
        while current_index < index - 1 and current_node is not None:
            current_node = current_node.next
            current_index += 1

        ### I have to check if the node at index-1 is none and if the next node is none. Crucial: current_node.next (the one to be removed) cant be none, as I would try to remove a node thats not none
        if current_node is None or current_node.next is None:
            return

        ###here I know that current_node at index-1 is not None and the one I want to remove at "index" called current_node.next exists.
        # test if there is a next node after the one I want to remove
        if current_node.next.next is None:
            current_node.next = None
            ###always adjust the tail when removing!!
            self.tail = current_node

        else:  ###no need to adjust the tail!
            current_node.next = current_node.next.next
            ##important: current node next already points to the next next, hence current_node.next.prev is the prev of the before called current_node.next.next
            current_node.next.prev = current_node

        self.length -= 1
