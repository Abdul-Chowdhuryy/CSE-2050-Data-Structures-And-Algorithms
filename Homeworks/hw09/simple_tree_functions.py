class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.data})"


def height(t):
    """Returns height tree
    """
    if t is None:
        return -1
    else:
        left_height = height(t.left)
        right_height = height(t.right)
        return max(left_height, right_height) + 1


def size(t):
    """Returns num nodes in tree
    """
    if t is None:
        return 0
    else:
        return size(t.left) + size(t.right) + 1


def find_min(t):
    """Returns the min element within a node in the tree"""
    if t is None:
        return float("inf")
    else:
        return min(t.data, find_min(t.left), find_min(t.right))


def find_max(t):
    """Returns the max element  within a node in the tree
    """
    if t is None:
        return float("-inf")
    else:
        return max(t.data, find_max(t.left), find_max(t.right))


def contains(t, k):
    """Returns True if k is contained within one of the nodes
    """
    if t is None:
        return False
    elif t.data == k:
        return True
    else:
        return contains(t.left, k) or contains(t.right, k)


def in_order(t):
    """Returns a list of contents of diff nodes in the tree in in-order traversal order.
    """
    if t is None:
        return []
    else:
        return in_order(t.left) + [t.data] + in_order(t.right)


def pre_order(t):
    """Returns a list of contents of diff nodes in the tree in pre-order traversal order.
    """
    if t is None:
        return []
    else:
        return [t.data] + pre_order(t.left) + pre_order(t.right)


def post_order(t):
    """Returns a list of contents of diff nodes in the tree in post-order traversal order.
    """
    if t is None:
        return []
    else:
        return post_order(t.left) + post_order(t.right) + [t.data]
