import unittest

from done.easy.climbingStairs import climb_stairs


class ClimbingStairsTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(0, climb_stairs(0))

    def test2(self):
        self.assertEqual(1, climb_stairs(1))

    def test3(self):
        self.assertEqual(2, climb_stairs(2))

    def test4(self):
        self.assertEqual(3, climb_stairs(3))

    def test5(self):
        self.assertEqual(5, climb_stairs(4))

    def test6(self):
        self.assertEqual(8, climb_stairs(5))

    def test7(self):
        self.assertEqual(13, climb_stairs(6))

    def test8(self):
        self.assertEqual(21, climb_stairs(7))

    def test9(self):
        self.assertEqual(34, climb_stairs(8))

    def test10(self):
        self.assertEqual(55, climb_stairs(9))
