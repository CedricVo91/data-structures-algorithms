class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class BST:  # right side always increases and left side always decreases
    def __init__(self, root):
        self.root = root

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return

        current_node = self.root

        while (
            True
        ):  # use this boolean helper function to create a repeated while loop with if statements
            if value < current_node.value:
                if current_node.left is None:
                    current_node.left = Node(value)
                    break
                else:
                    current_node = current_node.left
            elif value > current_node.value:
                if current_node.right is None:
                    current_node.right = Node(value)
                    break
                else:
                    current_node = current_node.right
            else:
                break  # I just want to exit the while loop without adding the same node value again.

    def lookup(self, value):
        # assuming a balanced bst
        current_node = self.root
        while (
            current_node
        ):  ##use the while true architecture to make it smoother to avoid the "none" situation below
            if value == current_node.value:
                return True
            elif value < current_node.value:
                current_node = (
                    current_node.left
                )  ## if the value does not exist, then either this eventually will become none
            else:
                current_node = (
                    current_node.right
                )  ## or this eventually will become none

        return False

    def remove(self, value):
        if self.root is None:
            return "Tree is empty"

        current_node = self.root
        ##come up with a parent node placeholder
        parent_node = None
        # first traverse the tree', then once found, there are three decisions to be made: no children, just adjust the node before, one child just connect the parent with the grandchildren,
        # complex case: two children: go for the right hand sides smallest value and repeat this for the adjustments in right hand side
        while current_node:
            if value < current_node.value:
                parent_node = current_node  # keeping track of head nodes
                current_node = current_node.left

            elif value > current_node.value:
                parent_node = current_node  # keeping track of head nodes
                current_node = current_node.right

            else:  # we only enter this else statement, if the node is found
                ## pattern: use an if statement inside an else statement when the else statement has many more subproblems and elifs would be too much

                ##start with simples case: node to be removed has no children
                if current_node.left is None and current_node.right is None:
                    # current node becomes parent node and hence gets "deleted"
                    ###current_node = parent_node -> not needed as we do not keep track of current node to readjust, we focus on its parent node and unlink the parent node to the current node to be removed
                    # edge case: # The node to be removed is the root node and it's a leaf
                    if (
                        parent_node is None
                    ):  # if a node has no parents it is the root node i.e. the parent of all parents.
                        self.root = None

                    # I need to adjust the children of the parent_node, but how do I now if the parent node before had a right or left node to get to the node to be removed?
                    if value < parent_node.value:
                        parent_node.left = None
                    else:
                        parent_node.right = None
                    return "Node removed"

                # second most difficult case: the current node has one child node
                elif current_node.left is None or current_node.right is None:
                    child_node = (
                        current_node.left if current_node.left else current_node.right
                    )  ###use this elegant way to make life easier with list comprehension

                    if parent_node is None:  # our selected node is the root node
                        self.root = child_node
                    # check if the node to be removed is left of the parent or right, regardless of the childnode of current node is left or right (could be true in both cases i.e. current node is on the right hand side or left hand side of the parent node)
                    elif value < parent_node.value:
                        # we know we are on the left hand side of the parent node
                        parent_node.left = child_node
                    else:
                        parent_node.right = child_node
                    return "Node removed"

                # most complex case: we have two child nodes and need to get the node on the right side and then left if it exists as the new child node
                # helper function to dynamically redefine the child node
                ###we need to redefine this dynamically that the child node becomes the smallest node in the right subtree. Our initial code just solved situation where it was the current node right left but not always the case that tree looks that simple
                # find the in order successor
                # keep track of the parent of the inorder successor
                successor_parent = current_node
                # go once right
                in_order_successor = current_node.right
                # traverse the left nodes until the last node
                while in_order_successor.left:
                    # keep track of the parent of the inorder_successor
                    successor_parent = in_order_successor
                    in_order_successor = in_order_successor.left
                # reset the current node value with the in order successor value to keep the structure of the tree i.e. the parent node of the value to be removed still points to the new node without doing the work of resetting
                current_node.value = (
                    in_order_successor.value
                )  # we have merely adjusted the value and not the tree structure. current_node.right is sill the same as before i.e. tree is the same

                # we have to get rid of the in order successor as it would be duplicates
                # two cases: 1) normal case where we have left nodes after the first right noe
                # 2) there are no left nodes for the first right node -> in order successor = current_node.right
                # 1) we have a left child -> in order successor = the leftest node on the right side of bst. It could or could not have a right child

                # 1) in order successor points to the leftest node and successor parent is the right node above
                # if in_order_successor.right: #if it has a right child
                #   successor_parent.left = in_order_successor.right #its always the left side of the parent
                # else:
                #   successor_parent.left = None

                # 2) in_order_successor = current_node.right
                # if in_order_successor.right:
                # successor parent will
                #   current_node.right =  in_order_successor.right
                # else:
                #   current_node.right = None

                # the code above is almost correct, but it can be combined into a simpler version of code according to chat gpt but I find it all too hard for now:

                # Check if in_order_successor is the immediate right child of current_node
                if successor_parent == current_node:
                    # The in-order successor is the immediate right child
                    current_node.right = (
                        in_order_successor.right
                    )  # we merely update the right child of the node instead of removing it. Same as the value reassignment
                else:
                    # The in-order successor was reached by moving left
                    successor_parent.left = (
                        in_order_successor.right
                    )  # if we do not have a right child the second part of equation is None

                return "Node removed"

        return "Node not found in the BST."

    #        4       20
    #     1    6   15  170


def print_tree(node, level=0, prefix="Root: "):
    if node is not None:
        print(" " * (level * 4) + prefix + str(node.value))
        if node.left is not None or node.right is not None:
            if node.left:
                print_tree(node.left, level + 1, "L--- ")
            else:
                print(" " * ((level + 1) * 4) + "L--- None")
            if node.right:
                print_tree(node.right, level + 1, "R--- ")
            else:
                print(" " * ((level + 1) * 4) + "R--- None")


# Example usage:
bst = BST(Node(10))
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)
bst.insert(12)
bst.insert(18)

print_tree(bst.root)

print(bst.lookup(12))

bst.remove(15)

print_tree(bst.root)
