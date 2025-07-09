from UniqueLinkedList import UniqueLinkedList

class LinearProbingHashTable:
    def __init__(self, MINBUCKETS=2, MINLOADFACTOR=0.1, MAXLOADFACTOR=0.9):
        """
        Initializes a Linear Probing Hash Table.

        """
        self.MINBUCKETS = MINBUCKETS
        self.MINLOADFACTOR = MINLOADFACTOR
        self.MAXLOADFACTOR = MAXLOADFACTOR
        self._buckets = [None] * MINBUCKETS
        self._size = 0  
    def __len__(self):
        """
        Returns the number of key-value pairs in the hash table.
        """
        return self._size
    
    def _hash_function(self, key):
        """
        Returns the hash value of the given key.
        """
        return hash(key) % len(self._buckets)

    def _probe_next_empty(self, index):
        """
        Finds the next empty slot in the bucket starting from the given index.
        """
        i = index
        while self._buckets[i] is not None and self._buckets[i] != -1:
            i = (i + 1) % len(self._buckets)
        return i

    def __setitem__(self, key, value):
        """
        Adds or updates a (key, value) pair in the hash table using linear probing.
        """
        index = self._hash_function(key)
        while self._buckets[index] is not None and self._buckets[index] != -1:
            if self._buckets[index][0] == key:
                self._buckets[index] = (key, value)
                return
            index = (index + 1) % len(self._buckets)
        self._buckets[index] = (key, value)
        self._size += 1

    def __getitem__(self, key):
        """
        Retrieves the value associated with the given key.
        """
        index = self._hash_function(key)
        while self._buckets[index] is not None:
            if self._buckets[index][0] == key:
                return self._buckets[index][1]
            index = (index + 1) % len(self._buckets)
        raise KeyError(key)

    def __contains__(self, key):
        """
        Checks if the hash table contains the given key.
        """
        index = self._hash_function(key)
        while self._buckets[index] is not None:
            if self._buckets[index][0] == key:
                return True
            index = (index + 1) % len(self._buckets)
        return False

    def pop(self, key):
        """
        Removes the (key, value) pair from the hash table and returns the value.

        """
        index = self._hash_function(key)
        while self._buckets[index] is not None:
            if self._buckets[index][0] == key:
                value = self._buckets[index][1]
                self._buckets[index] = -1 
                self._size -= 1
                return value
            index = (index + 1) % len(self._buckets)
        raise KeyError(key)

    def get_loadfactor(self):
        """
        Returns the current load factor of the hash table.

        """
        return self._size / len(self._buckets)
