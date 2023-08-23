import unittest
from factorial_recursive import factorial, print_factorial_sequence

class test_is_factorial(unittest.TestCase):
    def test_is_factorial (self):
        self.assertEqual(factorial(5),120)


class test_is_not_factorial(unittest.TestCase):
    def test_is_not_factorial (self):
        self.assertNotEqual (factorial(5),121)

class test_print_sequence(unittest.TestCase):
    def test_print_sequence (self):
        self.assertEqual(print_factorial_sequence(5),"The sequence: 5 x 4 x 3 x 2 x 1")


if __name__ == '__main__':
    unittest.main()
