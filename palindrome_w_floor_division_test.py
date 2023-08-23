import unittest
from palindrome_w_floor_division import is_palindrome

class test_is_palindrome(unittest.TestCase):
    def test_is_palindrome(self):
        #result = is_palindrome('radar')
        #self.assertTrue(result)
        self.assertTrue(is_palindrome('radar'),'radar')

class test_is_palindrome_negative(unittest.TestCase):
    def test_is_palindrome_negative(self):
        #result = is_palindrome('radar')
        #self.assertTrue(result)
        self.assertFalse(is_palindrome('HELLO'),'HELLO')

if __name__  == '__main__':
    unittest.main()