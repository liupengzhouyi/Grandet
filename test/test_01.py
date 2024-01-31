import unittest

class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

# test
class TestCalculator(unittest.TestCase):
    def test_add(self):
        result = Calculator.add(2, 3)
        self.assertEqual(result, 5)

    def test_subtract(self):
        result = Calculator.subtract(5, 3)
        self.assertEqual(result, 2)
    
    def test_subtract1(self):
        result = Calculator.subtract(5, 3)
        self.assertEqual(result, 2)
        
    def test_subtract3(self):
        result = Calculator.subtract(5, 3)
        self.assertEqual(result, 2)
    
    def test_subtract4(self):
        result = Calculator.subtract(5, 3)
        self.assertEqual(result, 2)
