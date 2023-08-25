import unittest
from palindrome_w_slice_notation import is_palindrome

class test_is_palindrome_positive(unittest.TestCase):
    def test_is_palindrome (self): 
        self.assertTrue(is_palindrome('radar'))

class test_is_palindrome_negative(unittest.TestCase):
    def test_is_palindrome (self): 
        self.assertFalse(is_palindrome('hello'))

###########################
if __name__ == '__main__':#
    unittest.main()       #
###########################