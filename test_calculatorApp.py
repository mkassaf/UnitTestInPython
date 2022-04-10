import unittest
from calculatorApp import *

class TestStringMethods(unittest.TestCase):

    def test_AddPass(self):
        self.assertEqual(calculate('1',2,3), 5)

    def test_AddInvalid(self):
        self.assertNotEqual(calculate('1',2,3), 9)

    def test_DividByZerror(self):
         with self.assertRaises(ValueError):
             calculate('4','3','w')


if __name__ == '__main__':
	unittest.main()
