from linkedlist import Node, LinkedList # get linkedlist.py from lab

class ReversableLinkedList(LinkedList):
    def reverse(self):
        """This function reverses the Linked List"""
        original_head = self._head
        prev_node = None
        current = self._head
        linkednode = None
        while current is not None:
            linkednode = current.link
            current.link = prev_node
            prev_node = current
            current = linkednode
        self._head = prev_node
        self._tail = original_head
        self._tail.link = None
      


class SortedLinkedList(LinkedList):
     def add_first(self, item):

        """This add_first method raises an implementation error from superclass"""

        raise NotImplementedError(f"Useadd_sorted({item})instead")
     def add_last(self, item):

        """This add_last method raises an implementation error from superclass"""

        raise NotImplementedError(f"Useadd_sorted({item})instead")
     def add_sorted(self, item):
        """This function adds an item to  sorted Linked List"""
        new_node = Node(item)
        current = self._head
        if self._head is None:
            self._head = new_node
            self._tail = new_node
        elif item <= self._head.item:
            new_node.link = self._head
            self._head.prev = new_node
            self._head = new_node
        else:
            current = self._head
            while current.link is not None and current.link.item < item:
                current = current.link
            new_node.link = current.link
            new_node.prev = current
            if current.link is not None:
                current.link.prev = new_node
            else:
                self._tail = new_node
            current.link = new_node
        self._len +=1
class UniqueLinkedList(LinkedList):
    def remove_dups(self):
        """This function removes duplicate nodes from Linked List"""
        items = {}
        current = self._head
        prev_node = None
        while current is not None:
            if current.item not in items:
                items[current.item] = 0
                prev_node = current
                current = current.link
            else:
                items[current.item] += 1
                prev_node.link = current.link
                current = current.link
                self._len -= 1
        return items

    
