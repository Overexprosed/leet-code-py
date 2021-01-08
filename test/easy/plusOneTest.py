import unittest

from done.easy.plusOne import plus_one


class PlusOneTest(unittest.TestCase):
    def test1(self):
        self.assertEqual([1, 2, 4], plus_one([1, 2, 3]))

    def test2(self):
        self.assertEqual([4, 3, 2, 2], plus_one([4, 3, 2, 1]))

    def test3(self):
        self.assertEqual([1], plus_one([0]))

    def test4(self):
        self.assertEqual([1, 0], plus_one([9]))
