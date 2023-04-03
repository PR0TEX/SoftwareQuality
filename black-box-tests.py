import unittest
import numpy

class TestRoundingNumber(unittest.TestCase):
    
    def test_round_two_decimal_places(self):
        test_input = 100.123
        expected_result = 100.12
        
        result = numpy.around(test_input,2)
        self.assertEqual(result, expected_result)
    
    def test_floor_rounding(self):
        test_input = 100.54
        expected_result = 100
        
        result = numpy.floor(test_input)
        self.assertEqual(result, expected_result)
        
class TestTrigonometricFunctions(unittest.TestCase):
    
    def test_sin(self):
        test_input = numpy.pi/2
        expected_result = 1
        
        result = numpy.sin(test_input)
        self.assertEqual(result, expected_result)
        
    def test_cos(self):
        test_input = numpy.pi/3
        expected_result = 0.5
        
        result = numpy.cos(test_input)
        self.assertEqual(numpy.round(result,2), expected_result)
    
    def test_tan(self):
        test_input = 0
        expected_result = 0
        
        result = numpy.tan(test_input)
        self.assertEqual(result, expected_result)
        
class TestArrayOperations(unittest.TestCase):
    
    def test_array_sum(self):
        test_input = [0.5, 1.5, 2.0, 1.5]
        expected_result = 5.5
        
        result = numpy.sum(test_input)
        self.assertEqual(result, expected_result)
    
class TestLogOperations(unittest.TestCase):
    
    def test_log10(self):
        test_input = 100
        expected_result = 2
        
        result = numpy.log10(test_input)
        self.assertEqual(result, expected_result)
        
    def test_log2(self):
        test_input = 8
        expected_result = 3
        
        result = numpy.log2(test_input)
        self.assertEqual(result, expected_result)
        
    def test_log(self):
        test_input = numpy.e
        expected_result = 1
        
        result = numpy.log(test_input)
        self.assertEqual(result, expected_result)
    
    def test_log1p(self):
        test_input = 1e-99
        expected_result = 1e-99
        
        result = numpy.log1p(test_input)
        self.assertEqual(result, expected_result)
        
class TestArithmeticOperations(unittest.TestCase):
    
    def test_add_numbers(self):
        test_input_a = 5
        test_input_b = 7
        expected_result = 12
        
        result = numpy.add(test_input_a, test_input_b)
        self.assertEqual(result, expected_result)
    
    def test_positive(self):
        test_input = [-1, -2, 5, 3]
        expected_result = [-1, -2, 5, 3]
        
        result = numpy.positive(test_input)
        numpy.testing.assert_array_equal(result, expected_result) 
        
    def test_negative(self):
        test_input = [-1, -2, 5, 3]
        expected_result = [1, 2, -5, -3]
        
        result = numpy.negative(test_input)
        numpy.testing.assert_array_equal(result, expected_result)
        
    def test_multiply(self):
        test_input_a = 5
        test_input_b = 5
        expected_result = 25
        
        result = numpy.multiply(test_input_a, test_input_b)
        self.assertEqual(result, expected_result)
        
    def test_divide(self):
        test_input_a = 50
        test_input_b = 10
        expected_result = 5
        
        result = numpy.divide(test_input_a, test_input_b)
        self.assertEqual(result, expected_result)
    
    def test_power(self):
        test_base = [0, 1, 2, 3, 4]
        test_exponent = 2
        expected_result = [0, 1, 4, 9, 16]
        
        result = numpy.power(test_base, test_exponent)
        numpy.testing.assert_array_equal(result, expected_result)
        
if __name__ == '__main__':
    unittest.main()