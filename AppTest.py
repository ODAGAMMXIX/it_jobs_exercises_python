# import obrigatorio
import unittest 
from App import upper, isEven
# o nome 'testStringMethods' pode mudar, mas o resto da linha é obrigatorio
class TestStringMethods(unittest.TestCase):
    # o nome de funções teste costumar ser test_*, onde * geralmente é a função testada
    def test_upper(self):
        # o assertEquals é um método para fazer asserção de valores, mas há outras variações (assertTrue, assertFalse)
        self.assertEqual(upper('foo'), 'FOO')

    def test_is_even(self):
        self.assertTrue(isEven(2))

    def test_is_not_even(self):
        self.assertFalse(isEven(3))    

## esse bloco é obrigatorio
if __name__ == '__main__':
    unittest.main()


# FONTE: https://docs.python.org/3/library/unittest.html