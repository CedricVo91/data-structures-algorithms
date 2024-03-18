class Node:
    def __init__(self, val, left, right):
        self.value = val
        self.left = left
        self.right = right


# the term "successor" refers to the node that can replace the deleted node while maintaining the BST's properties
# The successor of a node in a BST is the node with the smallest value that is greater than the value of the node to be deleted
def bst_delete(tree: Node, val: int) -> Node:

    #helper function to recursively find the node if it exists
    def find_and_modify(tree, val):

        if tree is None:
            return tree  # by this we ensure that we do not have a node with the tb deleted node, we return our original tree

        if tree.val == val:
            
            if tree.left: #there is a left child, so in any case we a
            
            if tree.right:
                successor = tree.right
                while successor.left is not None:
                    successor = successor.left
                temp = tree.right
                tree = successor
                tree.left = temp
                tree.right = temp.right

            if     

            return tree

        if tree.val > val:
            return find_and_modify(
                tree.left, val
            )  
        
        else:
            return find_and_modify(tree.right, val)

    #we have the current tree node, in which we actually run the recursive helper function 
    if tree.val > val:
        tree.left = find_and_modify(tree.left, val)  

    elif tree.val < val:
        tree.right = find_and_modify(tree.right)     

    return tree  # we just give back the tree, no need to delete anything as the value is not there
