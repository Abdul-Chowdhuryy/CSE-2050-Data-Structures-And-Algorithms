class BSTNode:
    def __init__(self, key, left=None, right=None):
        """Construct a node. By default, left and right children are None"""
        self.key = key
        self.left = left
        self.right = right
    
    def __iter__(self):
        """Classical iteration. Creates a new iterator object, which takes O(n)
        to construct the in-order list then returns items one at a time.
        """
        return BSTNode_Iterator(self)

    def in_order(self):
        """Generator based iteration. We can return items as soon as we find them,
        and the recursive stack we've built stays in memory until the next call
        due to the `yield` keyword.
        """
        if self.left is not None:
            yield from self.left.in_order()   # recursively go left
        yield self.key                       # return this key
        if self.right is not None:
            yield from self.right.in_order()  # recursively go right

    def __repr__(self):
        return f"BSTNode(key={self.key})"  # Uncommented to provide a string representation of the node

    def put(self, key):
        """Insert a key into the BST."""
        if key < self.key:
            if self.left is None:
                self.left = BSTNode(key)
            else:
                self.left.put(key)
        elif key > self.key:
            if self.right is None:
                self.right = BSTNode(key)
            else:
                self.right.put(key)

    def pre_order(self):
        """Generator based pre-order traversal."""
        yield self.key
        if self.left is not None:
            yield from self.left.pre_order()
        if self.right is not None:
            yield from self.right.pre_order()

    def post_order(self):
        """Generator based post-order traversal."""
        if self.left is not None:
            yield from self.left.post_order()
        if self.right is not None:
            yield from self.right.post_order()
        yield self.key


class BSTNode_Iterator:
    def __init__(self, node):
        self.queue = []
        self.in_order(node) # Queues up the entire tree
        self.counter = 0

    # in_order traversal/queueing
    def in_order(self, node):
        if node.left is not None:
            self.in_order(node.left)
        self.queue.append(node)
        if node.right is not None:
            self.in_order(node.right)

    # Update counter, return item, repeat
    def __next__(self):
        if self.counter < len(self.queue):
            self.counter += 1
            return self.queue[self.counter-1].key
        
        raise StopIteration
