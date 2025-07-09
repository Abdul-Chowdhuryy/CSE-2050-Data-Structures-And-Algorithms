class UniqueRecursiveNode:
    def __init__(self, key, value, link=None):
        """Creates a new node with key:value pair"""
        self.key = key
        self.value = value
        self.link = link

    def __iter__(self):
        """Iterates over the linked list"""
        yield self.key, self.value                      # yield values from this node
        if self.link is not None: yield from self.link  # continue to yield from link

    def __eq__(self, other):
        """returns if two nodes have same key values"""
        return self.key == other.key 
    
    
    def __hash__(self):
        """returns if two nodes have same hash values"""
        return hash(self.key)
    
    def add(self, key, value):
        """updates value of node with key or addes a new node with key:value pair, as appropriate"""
        if self.key == key:
            self.value = value
            return 0
        elif self.link is None:
            self.link = UniqueRecursiveNode(key, value)
            return 1
        else:
            return self.link.add(key, value)


    def get(self, key):
        """Returns value associated with key, Raises a KeyError if key not foun"""
        if self.key == key:
            return self.value
        elif self.link is not None:
            return self.link.get(key)
        else:
            raise KeyError

    def remove(self, key):
        """removes node containing key and returns tuple of new_link, value"""
        if self.key == key:
           value = self.value
           new_link = self.link
           return new_link, value
        elif self.link is not None:
            return self.link.remove(key)
        else:
            raise KeyError
        
        
    def __contains__(self, key):
        """ returns True iff key is in the linked list starting at this node"""
        if self.key == key:
            return True
        elif self.link is not None:
            return key in self.link
        else:
            return False

##########################################
# DO NOT CHANGE ANYTHING BELOW THIS LINE #
##########################################
class UniqueLinkedList:
    def __init__(self, items=None):
        """Creates a new linked list with optional collection of items"""
        self._head = None
        self._len = 0

        # Sequentially add items if they were included
        if items is not None:
            for key, value in items:
                self.add(key, value)

    def __len__(self):
        """Returns number of nodes in ULL"""
        return self._len
    
    def get_head(self):
        """Returns key, value in head"""
        return (self._head.key, self._head.value) if self._head is not None else None
    
    def get_tail(self):
        """Returns key, value in tail"""
        # Edge case - empty ULL
        if len(self) == 0: return None

        # Find tail node
        tail = self._head
        while tail.link is not None:
            tail = tail.link
        
        # Return key, value pair
        return (tail.key, tail.value)
    
    def add(self, key, value):
        """Adds node with key:value pair, or updates value, as appropriate"""
        # Edge case - empty linked list
        if len(self) == 0:
            self._head = UniqueRecursiveNode(key, value)
            n_added = 1
        
        else:
            # Note how we use the return value from UniqueRecursiveNode.add()
            n_added = self._head.add(key, value)
        
        self._len += n_added
        return n_added

    def get(self, key):
        """Returns value associated with key"""
        if len(self) == 0: raise KeyError(f"key {key} not in ULL")
        return self._head.get(key)

    def remove(self, key):
        """Removes node with key and returns value"""
        if len(self) == 0: raise KeyError(f"key {key} not found")

        new_head, value = self._head.remove(key)
        self._head = new_head
        self._len -= 1
        return value

    def __contains__(self, key):
        """Returns True iff key in ULL"""
        return self._head is not None and key in self._head
    
    def __iter__(self):
        """Returns iterable over key:value pairs in ULL"""
        if self._head is not None: yield from self._head
