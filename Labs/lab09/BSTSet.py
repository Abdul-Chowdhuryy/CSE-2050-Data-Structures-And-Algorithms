from BSTNode import BSTNode  # Assuming BSTNode is in a separate module

class BSTSet:
    def __init__(self):
        self._head = None

    def __iter__(self):
        return iter(self._head)

    def in_order(self):
        yield from self._head.in_order()

    def put(self, key):
        """Insert a key into the BSTSet."""
        if self._head is None:
            self._head = BSTNode(key)
        else:
            self._head.put(key)

    def pre_order(self):
        """Generator based pre-order traversal."""
        if self._head is not None:
            yield from self._head.pre_order()

    def post_order(self):
        """Generator based post-order traversal."""
        if self._head is not None:
            yield from self._head.post_order()
