class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_balanced(tree: Node) -> bool:
    # WRITE YOUR BRILLIANT CODE HERE
    def max_depth(tree: Node) -> int:
        if tree is None:
            return 0
        left = max_depth(tree.left)
        right = max_depth(tree.right)
        return max(left, right) + 1

    if tree is None:
        return 1

    if abs(max_depth(tree.left) - max_depth(tree.right)) > 1:
        return False

    return is_balanced(tree.left) + is_balanced(tree.right) > 1
    # return is_balanced(tree.left) and is_balanced(tree.right)


"""
Correct but inefficient solution!

Problem
For each node: 
1. I repeat the max depth on its left and right children (left and right subtree) to check if its balanced
2. After 1) I traversed the entire tree, now with is_balanced I recursively calculate the max depth again with the same if condition above
"""
