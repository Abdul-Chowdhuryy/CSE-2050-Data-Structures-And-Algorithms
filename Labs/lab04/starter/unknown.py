class ListNode:
    def __init__(self, data, link = None):
        self.data = data # element to go through indexs
        self.link = link # element to go through next element
    pass

class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0

    def addfirst(self, item):
        self._head = ListNode(item, self._head)
        if self._tail is None:
            self._tail = self._head

    def addlast(self, item):
        if self._head is None:
            self.addfirst(item)
        else:
            self._tail.link = ListNode(item)
            self._tail = self._tail.link

    def removefirst(self):
        item = self._head.data
        self._head = self._head.link
        if self._head is None:
            self._tail = None
        return item

    def removelast(self):
        if self._head is self._tail:
            return self.removefirst()
        else:
            currentnode = self._head
            while currentnode.link is not self._tail:
                currentnode = currentnode.link
            item = self._tail.data
            self._tail = currentnode
            self._tail.link = None
            return item
    def __len__(self):
        return self._length




