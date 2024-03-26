class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def valid_bst(root: Node, min_val=float("-inf"), max_val=float("inf")) -> bool:
    # WRITE YOUR BRILLIANT CODE HERE

    ##if a none node is reached, its parent node does not violate the BST property regardless if it has a left child with a non None value.
    if root is None:
        return True

    ##important: BST property is like start a path at the root and keep track of the root's value. Left should be always less, right always bigger

    # check if the current root value violates the BST property
    if min_val >= root.val or root.val >= max_val:
        return False

    # this checks if the property is not validated in the subtrees of root
    left = valid_bst(root.left, min_val, root.val)
    right = valid_bst(root.right, root.val, max_val)

    if left is True and right is True:
        return True
    else:
        return False


def valid_bst_corr(root: Node) -> bool:
    # WRITE YOUR BRILLIANT CODE HERE
    def dfs(root: Node, min_val=float("-inf"), max_val=float("inf")) -> bool:

        if root is None:
            return True

        if root.val > min_val and root.val < max_val:
            left = dfs(root.left, min_val, root.val)
            right = dfs(root.right, root.val, max_val)
            return left and right

        return False

    return dfs(root)


# inserting into bst:
def insert_bst(bst: Node, val: int) -> Node:
    # WRITE YOUR BRILLIANT CODE HERE
    if bst is None:
        return Node(
            val
        )  # if we reached leaf, we want to return up the newly added Node

    if bst.val < val:
        bst.right = insert_bst(bst.right, val)

    elif (
        bst.val > val
    ):  # important to do an elif as otherwise it val is equal to an existing node val we don't return the original tree
        bst.left = insert_bst(bst.left, val)

    return bst
