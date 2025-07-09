class CustomSet:
    def __init__(self):
        """Initializes an empty CustomSet"""
        self._min_buckets = 8            # We never want to rehash down below this many buckets.
        self._n_buckets = 8              # initial size. Good to use a power of 2 here.
        self._len = 0                    # Number of items in custom set
        self._L = [[] for _ in range(self._n_buckets)]   # List of empty buckets

    def __len__(self):
        """Returns the number of items in CustomSet"""
        return self._len

    def _find_bucket(self, item):
        """Returns the index of the bucket `item` should go in, based on hash(item) and self.n_buckets"""
        return hash(item) % self._n_buckets

    def __contains__(self, item):
        """Returns True (False) if item is (is not) in the CustomSet"""
        location = self._find_bucket(item)
        bucket = self._L[location]
        for i in bucket:
            if item == i:
                return True
        return False

    def add(self, item):
        """Adds a new item to CustomSet. Duplicate adds are ignored."""
        if item not in self:
            location = self._find_bucket(item)
            self._L[location].append(item)
            self._len += 1
            if len(self) >= 2 * self._n_buckets:
                self._rehash(2 * self._n_buckets)

    def remove(self, item):
        """Removes item from CustomSet. Raises a KeyError if item is not in CustomSet."""
        if item not in self:
            raise KeyError(f"{item} not found in CustomSet")
        location = self._find_bucket(item)
        self._L[location].remove(item)
        self._len -= 1
        if len(self) <= 0.5 * self._n_buckets and 0.5 * self._n_buckets >= self._min_buckets:
            self._rehash(int(0.5 * self._n_buckets))

    def _rehash(self, new_buckets):
        """Rehashes items from a hash table with n_buckets to one with new_buckets."""
        new_L = [[] for _ in range(new_buckets)]
        for bucket in self._L:
            for item in bucket:
                new_location = hash(item) % new_buckets
                new_L[new_location].append(item)
        self._L = new_L
        self._n_buckets = new_buckets
