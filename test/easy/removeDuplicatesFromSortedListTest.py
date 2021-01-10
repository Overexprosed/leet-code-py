import unittest

from done.easy.data.ListNode import ListNode
from done.easy.removeDuplicatesFromSortedList import delete_duplicates


class RemoveDuplicatesFromSortedListTest(unittest.TestCase):
    def test1(self):
        test_node = ListNode(1, ListNode(1, ListNode(2)))
        expected_node = ListNode(1, ListNode(2))
        self.assertEqual(expected_node, delete_duplicates(test_node))

    def test2(self):
        test_node = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
        expected_node = ListNode(1, ListNode(2, ListNode(3)))
        self.assertEqual(expected_node, delete_duplicates(test_node))

    def test3(self):
        test_node = ListNode(1, ListNode(1, ListNode(1)))
        expected_node = ListNode(1)
        self.assertEqual(expected_node, delete_duplicates(test_node))

    def test4(self):
        test_node = ListNode(1)
        expected_node = ListNode(1)
        self.assertEqual(expected_node, delete_duplicates(test_node))

    def test5(self):
        test_node = ListNode(3, ListNode(3))
        expected_node = ListNode(3)
        self.assertEqual(expected_node, delete_duplicates(test_node))
