class Node:
    def __init__(self, val, left, right):
        self.value = val
        self.left = left
        self.right = right


# the term "successor" refers to the node that can replace the deleted node while maintaining the BST's properties
# The successor of a node in a BST is the node with the smallest value that is greater than the value of the node to be deleted
def bst_delete(tree: Node, val: int) -> Node:

    parent_node = None
    node_to_be_deleted = None
    parent_node_tobedeleted = None  # external variable to keep track of the parent node
    successor = None
    parent_successor = None

    def find(tree, val):

        if tree is None:
            return -1  # placeholder for False: no Node with such a val was found

        if tree.val == val:
            node_to_be_deleted = tree

            # get successor if there
            successor = tree.right.left
            while successor.left is not None:
                successor = successor.left
            return node_to_be_deleted, successor

        # if we havent found our node to be deleted, we have to go down left or right, and save our current parent node
        parent_node = tree

        if tree.val > val:
            return find(tree.left, val)

        else:
            return find(tree.right, val)

    if find(tree) == -1:
        return tree  # we just give back the tree, no need to delete anything as the value is not there

    node_to_be_deleted, parent_successor, successor = find(tree)
    ##reassign nodes
    # after that our parent node is the one before the node to be deleted
    if parent_node.val > val:
        parent_node.left = successor
        successor.right = node_to_be_deleted.right
        successor.left = node_to_be_deleted.left

    else:
        parent_node.right = successor
        successor.right = node_to_be_deleted.right
        successor.left = node_to_be_deleted.left
