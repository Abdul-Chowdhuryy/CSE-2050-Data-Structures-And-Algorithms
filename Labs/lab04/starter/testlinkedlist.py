import unittest
from linkedlist import Node
from linkedlist import LinkedList
class test_linkedlist(unittest.TestCase):
    def test_node(self, Node):
        node1 = Node("jake", None)
        self.assertEqual(node1.item, "jake")
        self.assertEqual(node1.link, None)
    def test_repr(self, Node):
        node1 = Node("jake", None)
        self.assertEqual(repr(node1), "Node(jake)")
        if __name__ == '__main__':
            unittest.main()
    def test_linkedlist(self):
        LL1 = LinkedList()
        
        self.assertEqual(len(LL1), 0)
        self.assertIsNone(LL1.get_head())
        self.assertIsNone(LL1.get_tail())
    def test_add_last(self):
        
        LL1 = LinkedList()

       
        items = [1, 2, 3, 4, 5]
        for item in items:
            LL1.add_last(item)

        self.assertEqual(len(LL1), len(items))
        self.assertEqual(LL1.get_head(), items[0])
        self.assertEqual(LL1.get_tail(), items[-1])
    def test_add_first(self):
        
        LL1 = LinkedList()

       
        items = [2, 3, 7, 8]
        for item in items:
            LL1.add_first(item)
        
        self.assertEqual(len(LL1), len(items))
        self.assertEqual(LL1.get_head(), items[0])
        self.assertEqual(LL1.get_tail(), items[-1])
    def test_remove_first(self):
        
        LL1 = LinkedList()
        items = [0, 1, 2, 3, 4]
        for item in items:
            LL1.add_last(item)

    
        for item in items:
            removed_item = LL1.remove_first()
            self.assertEqual(removed_item, item)
            self.assertEqual(len(LL1), len(items) - items.index(item) - 1)
            if len(LL1) > 0:
                self.assertEqual(LL1.get_head(), items[items.index(item) + 1])
            else:
                self.assertIsNone(LL1.get_head())
            if len(LL1) > 0:
                self.assertEqual(LL1.get_tail(), items[-1])
            else:
                self.assertIsNone(LL1.get_tail())
        
