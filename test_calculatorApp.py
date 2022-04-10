import unittest
from calculatorApp import *

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(calculate('1',2,3), 7)

    def test_upper2(self):
        self.assertEqual(calculate('1',2,3), 5)

