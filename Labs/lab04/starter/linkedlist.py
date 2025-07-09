from typing import Any, Optional, Iterable

class Node:
    def __init__(self, item=None, link=None):
        '''initalizing node, and link to node'''
        self.item = item
        self.link = link
    
    def __repr__(self):
        '''Test'''
        return f'Node({self.item})'

class LinkedList:
    def __init__(self, items: Optional[Iterable[Any]] = None):
        '''initlaizing the head, tail, and length'''
        self._head = None
        self._tail = None
        self._len = 0
        
        if items is not None:
            for item in items:
                self.add_last(item)
                
    def __len__(self):
        '''returning length of linked list'''
        return self._len
    
    def get_head(self) -> Any:
        '''returning head of node'''
        return self._head.item if self._head else None
    
    def get_tail(self) -> Any:
        '''returning tail of node'''
        return self._tail.item if self._tail else None
    
    def add_first(self, item: Any) -> None:
        '''adding item to beginning of node'''
        node = Node(item)
        if self._head is None:
            self._head = node
            self._tail = node
        else:
            node.link = self._head
            self._head = node
        self._len += 1
    
    def add_last(self, item: Any) -> None:
        '''adding item to end of node'''
        node = Node(item)
        if self._tail is None:
            self._head = node
            self._tail = node
        else:
            self._tail.link = node
            self._tail = node
        self._len += 1
    
    def remove_first(self) -> Any:
        '''removing head of node'''
        if self._head is None:
            raise RuntimeError("Cannot remove from an empty LinkedList")
        item = self._head.item
        if self._head is self._tail:
            self._head = None
            self._tail = None
        else:
            self._head = self._head.link
        self._len -= 1
        return item
    
    def remove_last(self) -> Any:
        '''removing tail of node'''
        if self._tail is None:
            raise RuntimeError("Cannot remove from an empty LinkedList")
        item = self._tail.item
        if self._head is self._tail:
            self._head = None
            self._tail = None
        else:
            current = self._head
            while current.link is not self._tail:
                current = current.link
            current.link = None
            self._tail = current
        self._len -= 1
        return item
