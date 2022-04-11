import unittest
from calculatorApp import *

class TestCalculate(unittest.TestCase):
    def setUp(self):
         print("Setup .. ")

    def test_AddPass(self):
        self.assertEqual(calculate('1',2,3), 5)

    def test_AddInvalid(self):
        self.assertNotEqual(calculate('1',2,3), 9)

    def test_DividByZerror(self):
        with self.assertRaises(ValueError):
             calculate('4','3','w')
        ##Or you can use this ##self.assertRaises(ValueError, calculate, '4','3','w') 

    def test_DividByZerrorRegex(self):
        with self.assertRaisesRegex(ValueError, "input is not a number!"):
             calculate('4','3','w')

    def tearDown(self):
        print("tearDown .. ")

if __name__ == '__main__':
	unittest.main()
