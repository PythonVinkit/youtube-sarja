import unittest
from .. import fibonacci


class TestFibonacci(unittest.TestCase):

    def test_correct_values_unittest(self):
        self.assertEqual(fibonacci.fibonacci_of(5), 5)
        self.assertEqual(fibonacci.fibonacci_of(6), 8)
        self.assertEqual(fibonacci.fibonacci_of(7), 13)

    def test_failed_typing_unittest(self):
        with self.assertRaises(ValueError):
            fibonacci.fibonacci_of('5')
