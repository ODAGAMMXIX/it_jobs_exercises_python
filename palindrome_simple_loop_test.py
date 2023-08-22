import unittest
from palindrome_simple_loop import is_palindrome

class test_is_palindrome(unittest.TestCase):    
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome('radar'))

    def test_is_not_palindrome(self):
        self.assertFalse(is_palindrome('bola'))      

if __name__ == '__main__':
    unittest.main()