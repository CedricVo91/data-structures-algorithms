class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root):
    # WRITE YOUR BRILLIANT CODE HERE
    if root is None:
        return "x"
    left = serialize(root.left)
    right = serialize(root.right)

    return (
        str(root.val) + " " + left + " " + right
    )  # important to use a delimiter here, otherwise one couldn't distinguish between one and two or more digit numbers for root values i.e. 3 vs 43


"""
Three deserialize Solutions: 
1. with pop() -> space complexity stays O(n) but time complexity increases as for each n recursive calls, we call pop which is O(n) as it shifts array/list in place
2. with indexing -> time complexity stays O(n) as it slides through the n nodes with each recursive call, but space complexity increases as for each recursive call we temporarily create a new list 
3. with iterator and next() -> best/preferred version
"""


def deserialize_pop(s):
    # get a list with the nodes values (str type) without the ","
    nodes_list = s.split(" ")

    # run dfs on the nodes defined in the nodes_list
    def dfs(nodes_list):

        # important! basecase for when we popped it all away
        if len(nodes_list) == 0:
            return None

        root_val = nodes_list.pop(0)
        if root_val == "x" or root_val == "X":
            return None
        else:
            root_val = int(root_val)

        left = dfs(nodes_list)
        right = dfs(nodes_list)

        return Node(root_val, left, right)

    return dfs(nodes_list)


def deserialize_iter(s):
    # get a list with the nodes values (str type) without the ","
    nodes_list = iter(s.split(" "))

    # run dfs on the nodes defined in the nodes_list
    def dfs(nodes_list):

        root_val = next(nodes_list)
        if root_val == "x" or root_val == "X":
            return None
        else:
            root_val = int(root_val)

        left = dfs(nodes_list)
        right = dfs(nodes_list)

        return Node(root_val, left, right)

    return dfs(nodes_list)


def deserialize_via_index(s):
    # get a list with the nodes values (str type) without the ","
    nodes_list = s.split(" ")  # creates list automatically
    i = 0

    # run dfs on the nodes defined in the nodes_list
    def dfs(nodes_list, i):

        root_val = nodes_list[i]
        i = i + 1
        if root_val == "x" or root_val == "X":
            return None, i
        else:
            root_val = int(root_val)

        left, i = dfs(nodes_list, i)

        right, i = dfs(nodes_list, i)

        return Node(root_val, left, right), i

    # so that solution still works in our implementation, we need to give the program the tree, not the index
    # tree is basically a linked lists of the nodes all pointing to each other in right sequence
    tree, _ = dfs(
        nodes_list, i
    )  # give us the node(root_val, left,right) and the left and right point to the right children
    return tree
