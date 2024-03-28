class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lca_on_bst(bst: Node, p: int, q: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    # before even going down the tree, we can set the default value of lca to be the root node as it will be the lca of any two nodes unless we update it on the way down
    # however, this default value of lca not needed as we can return up the lca
    def dfs(bst: Node, p: int, q: int):
        # when should we stop going down the tree? when we found the values p and q

        # edge case where p and q are not part of tree (i.e. bst.val never equals p or q) should happen per definition
        # if bst is None:
        #   return None

        # this would be store holder for when p is the parent of q and vice versa
        if bst.val == q or bst.val == p:
            lca = bst  # if q = 4 and p = 3 and we get to bst.val is root of right subtree (4,3,5), the lca becomes the bst,val
            return lca

        # p and q must be on the left subtree
        if bst.val > q and bst.val > p:
            # reset lca to be the root node of left tree
            lca = dfs(bst.left, p, q)
            return lca

        # p and q must be on the right subtree
        elif bst.val < q and bst.val < p:
            lca = dfs(bst.right, p, q)
            return lca
        # easiest case: if p and q are not on the same subtree, their lca is the root of the two subtrees
        else:
            lca = bst
            return lca

    return dfs(bst, p, q).val


def lca_on_bst(bst: Node, p: int, q: int) -> int:

    # edge case where p and q are not part of tree (i.e. bst.val never equals p or q) should happen per definition
    if bst is None:
        return None

    # p and q must be on the left subtree
    if bst.val > q and bst.val > p:
        # reset lca to be the root node of left tree
        lca = lca_on_bst(bst.left, p, q)
        # return lca

        # p and q must be on the right subtree
    elif bst.val < q and bst.val < p:
        lca = lca_on_bst(bst.right, p, q)
        # return lca

    ###the two statements if statements below are not needed anymore:
    ##simplify the code below -> just return lca as it will be lca in any case
    # else:
    #    lca = bst
    #    return lca

    ##simplify again:for case below we do not need an if statement, we just assign lca to bst
    # this would be store holder for when p is the parent of q and vice versa
    # if bst.val == q or bst.val == p:
    #    lca = bst  # if q = 4 and p = 3 and we get to bst.val is root of right subtree (4,3,5), the lca becomes the bst,val
    # return lca
    lca = bst

    # return the val of the node as this function is supposed to return an int value
    return lca.val


##most simplified version
def lca_on_bst(bst: Node, p: int, q: int) -> int:

    # edge case where p and q are not part of tree (i.e. bst.val never equals p or q) should happen per definition
    if bst is None:
        return None

    # p and q must be on the left subtree
    if bst.val > q and bst.val > p:
        return lca_on_bst(bst.left, p, q)

    # p and q must be on the right subtree
    elif bst.val < q and bst.val < p:
        return lca_on_bst(bst.right, p, q)

    ##simplification:
    # return the val of the node as this function is supposed to return an int value
    return bst.val
