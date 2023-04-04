import unittest
import numpy

class TestNumbersDivision(unittest.TestCase):
    def test_divide(self):
        test_input_a = 50
        test_input_b = 10
        expected_result = 5
        
        result = numpy.divide(test_input_a, test_input_b)
        self.assertEqual(result, expected_result)
        
if __name__ == '__main__':
    unittest.main()