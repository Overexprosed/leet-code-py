import unittest

from done.easy.sqrt import sqrt


class SqrtTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(2, sqrt(4))

    def test2(self):
        self.assertEqual(2, sqrt(8))

    def test3(self):
        self.assertEqual(10, sqrt(100))

    def test4(self):
        self.assertEqual(0, sqrt(0))

    def test5(self):
        self.assertEqual(1, sqrt(1))

    def test6(self):
        self.assertEqual(1, sqrt(2))
