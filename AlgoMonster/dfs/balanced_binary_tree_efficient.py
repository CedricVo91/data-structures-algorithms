class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth_is_balanced(tree: Node) -> int:
    # WRITE YOUR BRILLIANT CODE HERE

    if tree is None:
        return 0

    left = max_depth_is_balanced(tree.left)
    right = max_depth_is_balanced(tree.right)

    # check if any subtrees on the left or right is not balanced
    if left == -1 or right == -1:
        return -1

    # check for balanced tree in current node
    if abs(left - right) > 1:
        return -1

    # current tree and subtree is balanced, return the height
    return max(left, right) + 1


def is_balanced(tree: Node) -> bool:
    if max_depth_is_balanced(tree) != -1:
        return True


"""
whenever we are at a root node we first check if there are nodes
then we check if any left and right subtrees are balanced
then we check if the current roots tree is balanced i.e. the longest path of the left resp right tree are balanced when subtracting them 
if so, we know that all the sub trees are balanced and so is the current root/nodes tree and we return the max_depth


in this implementation we both check the height and balance at the same time
"""

"""
additional input: we return -1 as its an integer placeholder for false i.e. when its not balanced
reason: we cannot return both integers (height) and boolean values (False) -> return type confusion
"""

##alternative: returning a tuple with both type of return values


def max_depth_and_is_balanced(tree: Node) -> (bool, int):
    if tree is None:
        return True, 0  # An empty tree is balanced, with a depth of 0.

    left_balanced, left_depth = max_depth_and_is_balanced(tree.left)
    right_balanced, right_depth = max_depth_and_is_balanced(tree.right)

    # If either subtree is not balanced, the entire tree is not balanced.
    if not left_balanced or not right_balanced:
        return False, 0  # The depth is irrelevant here.

    # If the current node is balanced, check the height difference.
    if abs(left_depth - right_depth) > 1:
        return False, 0  # Again, depth is irrelevant if the tree is not balanced.

    # If the tree is balanced, return True and the correct depth.
    return True, max(left_depth, right_depth) + 1


def is_balanced(tree: Node) -> bool:
    balanced, _ = max_depth_and_is_balanced(tree)
    return balanced
