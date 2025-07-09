from UniqueLinkedList import UniqueLinkedList

class SeparateChainingHashTable:
    def __init__(self, MINBUCKETS=2, MINLOADFACTOR=0.5, MAXLOADFACTOR=1.5):
        """
        Initializes a Separate Chaining Hash Table.
        """
        self.MINBUCKETS = MINBUCKETS
        self.MINLOADFACTOR = MINLOADFACTOR
        self.MAXLOADFACTOR = MAXLOADFACTOR
        self._buckets = [UniqueLinkedList() for i in range(MINBUCKETS)]
        self._size = 0  

    def __len__(self):
        """
        Returns the number of key-value pairs in the hash table.
        """
        return self._size
    
    def _bucket(self, k):
        """
        Returns the bucket corresponding to the given key.

        
        """
        bucket_index = hash(k) % len(self._buckets)
        return self._buckets[bucket_index]
    
    def __setitem__(self, key, value):
        """
        Adds or updates a (key, value) pair in the hash table.

       
        """
        bucket = self._bucket(key)

        for record in bucket:
            if record.k == key:
                record.v = value
                return
        bucket.add(key, value)
        self._size += 1

    def __getitem__(self, key):
        """
        Retrieves the value associated with the given key.

        """
        bucket = self._bucket(key)

        for record in bucket:
            if record.k == key:
                return record.v
        raise KeyError(key)

    def __contains__(self, key):
        """
        Checks if the hash table contains the given key.

        """
        bucket = self._bucket(key)

        for record in bucket:
            if record.k == key:
                return True
        return False

    def pop(self, key):
        """
        Removes the (key, value) pair from the hash table and returns the value.

        """
        bucket = self._bucket(key)

        for i, record in enumerate(bucket):
            if record.k == key:
                value = record.v
                bucket.remove_at_index(i)
                self._size -= 1
                return value
        raise KeyError(key)

    def get_loadfactor(self):
        """
        Returns the current load factor of the hash table.

        """
        return self._size / len(self._buckets)
