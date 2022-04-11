import unittest
from unittest import mock
from unittest.mock import patch
from calculatorApp import *
import calculatorApp
class TestCalculate(unittest.TestCase):
    def setUp(self):
        print("Setup .. ")
        self.patcher1 = patch('calculatorApp.add', return_value = 5)
        self.MockClass1 = self.patcher1.start()

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

    
    def test_AddPassWithMockEx1(self):
        with mock.patch('calculatorApp.add', return_value = 5):
            result = calculate('1',2,2)
        self.assertEqual(result, 5)

    @mock.patch('calculatorApp.add', return_value = 5)
    def test_AddPassWithMockEx2(self, mock_check):
        result = calculate('1',2,2)
        self.assertEqual(result, 5)


    def test_AddPassWithMocEx3(self):
        assert calculatorApp.add is self.MockClass1
        self.assertEqual(calculate('1',2,3), 5)

    def tearDown(self):
        print("tearDown .. ")
        self.patcher1.stop()

if __name__ == '__main__':
	unittest.main()
