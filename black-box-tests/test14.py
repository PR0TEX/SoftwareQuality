import unittest
import numpy

class TestNumbersMultiplication(unittest.TestCase):
    def test_multiply(self):
        test_input_a = 5
        test_input_b = 5
        expected_result = 25
        
        result = numpy.multiply(test_input_a, test_input_b)
        self.assertEqual(result, expected_result)
        
if __name__ == '__main__':
    unittest.main()