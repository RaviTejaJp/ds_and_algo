"""Test Cases for Doubly linked lists

"""
import sys
import os
import unittest

file_path = os.path.dirname(os.path.abspath(__file__).replace("tests",""))
sys.path.insert(0, file_path)

from src import *


class DoublyLinkedListTest(unittest.TestCase):
    def setUp(self) -> None:
        self.node_1 = DoublyLinkedListNode(1)
        self.node_2 = DoublyLinkedListNode(2)
        self.node_3 = DoublyLinkedListNode(3)
        
        self.dll = DoublyLinkedList()
    
    def test_empty_dll(self):
        self.assertListEqual(self.dll.to_list(), [])

    def test_single_node_dll(self):
        self.dll.append_node(DoublyLinkedListNode(1))
        self.assertListEqual(self.dll.to_list(), [1])

    def test_two_node_dll(self):
        self.dll.append_node(DoublyLinkedListNode(1))
        self.dll.append_node(DoublyLinkedListNode(2))
        self.assertListEqual(self.dll.to_list(), [1,2])
    
    def test_append_value_dll(self):
        self.dll.append_node(DoublyLinkedListNode(1))
        self.dll.append_node(DoublyLinkedListNode(2))
        self.dll.append(DoublyLinkedListNode(3))
        self.dll.append(4)
        self.assertListEqual(self.dll.to_list(), [1,2,3,4])

    def test_prepend_node_dll(self):
        self.dll.prepend_node(DoublyLinkedListNode(1))
        self.dll.prepend_node(DoublyLinkedListNode(2))
        self.dll.prepend_node(DoublyLinkedListNode(3))
        self.dll.prepend(4)
        self.assertListEqual(self.dll.to_list(), [4,3,2,1])



if __name__ == '__main__':
    unittest.main()