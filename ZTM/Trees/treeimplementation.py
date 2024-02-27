class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class BST:  # right side always increases and left side always decreases
    def __init__(self, root):
        self.root = root

    def insert(self, value):
        current_node = self.root

        if self.root.value is None:
            self.root = Node(value)
            print(self.root.value)
            return  ##exit the function once inserted

        while value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
                print(current_node.left.value)
                break  ##break the loop as we have successfully inserted the node
            else:
                current_node = current_node.left
                print(current_node.value)

        while value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
                print(current_node.right.value)
                break  ##break the while loop to stop as we achieved our goal to insert the node
            else:
                current_node = current_node.right
                print(current_node.value)

    def lookup(value):
        pass

    def remove(value):
        pass

    #            9
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

"""the problem with the code above is that it only works in a sequential manner i.e. once we get to a point where a node is larger than root node, 
but smaller then root node right, we are already in the second while loop (as we are in the right node of the root node).
we end this while loop by setting the current node to the current_node.right and our value is per default smaller than the new current node right"""
