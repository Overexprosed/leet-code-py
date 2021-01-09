import unittest

from done.easy.fibonacciNumber import fib


class FibonacciNumberTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(0, fib(0))

    def test2(self):
        self.assertEqual(1, fib(1))

    def test3(self):
        self.assertEqual(1, fib(2))

    def test4(self):
        self.assertEqual(2, fib(3))

    def test5(self):
        self.assertEqual(3, fib(4))

    def test6(self):
        self.assertEqual(5, fib(5))

    def test7(self):
        self.assertEqual(8, fib(6))

    def test8(self):
        self.assertEqual(13, fib(7))

    def test9(self):
        self.assertEqual(21, fib(8))

    def test10(self):
        self.assertEqual(34, fib(9))

    def test11(self):
        self.assertEqual(55, fib(10))

    def test12(self):
        self.assertEqual(832040, fib(30))
