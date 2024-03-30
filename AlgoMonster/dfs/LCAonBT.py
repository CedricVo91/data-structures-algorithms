class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lca(root, node1, node2):
    # WRITE YOUR BRILLIANT CODE HERE

    # we went down a subtree and found out that on that subtree does not contain the two values i.e. they are on the left one
    if root is None:
        return None

    # first simple case: the root node of the BT is one of the nodes
    if root in (node1, node2):
        return root

    # second simple case: the root is the lca of node 1 and node2:
    if root.left in (node1, node2) and root.right in (node1, node2):
        return root

    # more difficult cases: either the left or right child of root is on the second level or the nodes lie on the third level of the tree or lower
    # case 4:
    # the left node is one of the node to be looked for and hence the lca
    elif root.left in (
        node1,
        node2,
    ):  # this directly assumes that root.right is not in (node1,node2)
        return root.left

    elif root.right in (node1, node2):
        return root.right

    else:
        left = lca(root.left, node1, node2)
        right = lca(root.right, node1, node2)

        if left is None:
            return right
        elif right is None:
            return left
        else:  # two two nodes are in different sub trees
            return root
