class Node:
    def __init__(self, val, left, right):
        self.value = val
        self.left = left
        self.right = right


# the term "successor" refers to the node that can replace the deleted node while maintaining the BST's properties
# The successor of a node in a BST is the node with the smallest value that is greater than the value of the node to be deleted
def bst_delete(tree: Node, val: int) -> Node:

    # helper function to recursively find the node if it exists
    def find_and_modify(tree, val):

        if tree is None:
            return tree  # by this we ensure that we do not have a node with the tb deleted node, we return our original tree

        if tree.val == val:

            if (
                tree.left is None
            ):  # there is a no left child, we only have at best a right child
                return tree.right

            elif (
                tree.right is None
            ):  # there is a no right child, we only have at best a left child
                return tree.left

            # two children. no else is needed as we have two return statements in the if/elif clause
            successor = tree.right
            while successor.left is not None:
                successor = successor.left

            # the trickiest part: instead of switching nodes, we just amend the values and keep the left and right child
            tree.val = successor.val
            # left child of tree is still linked correctly
            # adjust right child of tree by running the find and modify (aka delete function again) with value of successor
            tree.right = find_and_modify(tree.right, successor.val)

            return tree

        elif tree.val > val:
            return find_and_modify(tree.left, val)

        else:
            return find_and_modify(tree.right, val)

    return find_and_modify(tree, val)


# helper function to recursively find the node if it exists
def bst_delete(tree: Node, val: int) -> Node:

    if tree is None:
        return tree  # by this we ensure that we do not have a node with the tb deleted node, we return our original tree

    if tree.val == val:

        if (
            tree.left is None
        ):  # there is a no left child, we only have at best a right child
            return tree.right

        elif (
            tree.right is None
        ):  # there is a no right child, we only have at best a left child
            return tree.left

        # two children. no else is needed as we have two return statements in the if/elif clause
        successor = tree.right
        while successor.left is not None:
            successor = successor.left

        # the trickiest part: instead of switching nodes, we just amend the values and keep the left and right child
        tree.val = successor.val
        # left child of tree is still linked correctly
        # adjust right child of tree by running the find and modify (aka delete function again) with value of successor
        tree.right = bst_delete(tree.right, successor.val)

        return tree

    elif tree.val > val:
        return bst_delete(tree.left, val)

    else:
        return bst_delete(tree.right, val)
