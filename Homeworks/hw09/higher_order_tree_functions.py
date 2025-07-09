class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.data})"

############################################
### Please do not alter the above class. ###
############################################

def count_failures(pred, t):
    """Counts the num of nodes in the tree"""
    if t is None:
        return 0
    else:
        failures = pred(t.data)
        left_count = count_failures(pred, t.left)
        right_count = count_failures(pred, t.right)
        return failures + left_count + right_count

def tree_map(f, t):
    """Returns a new tree consisting of new nodes
    """
    if t is None:
        return None
    else:
        mapped_left = tree_map(f, t.left)
        mapped_right = tree_map(f, t.right)
        return TreeNode(f(t.data), left=mapped_left, right=mapped_right)

def tree_apply(f, t):
    """Applies each node of the tree
    """
    if t is not None:
        t.data = f(t.data)
        tree_apply(f, t.left)
        tree_apply(f, t.right)
