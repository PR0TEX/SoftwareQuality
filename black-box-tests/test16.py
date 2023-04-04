import unittest
import numpy

class TestNumberPower(unittest.TestCase):
    def test_power(self):
        test_base = [0, 1, 2, 3, 4]
        test_exponent = 2
        expected_result = [0, 1, 4, 9, 16]
        
        result = numpy.power(test_base, test_exponent)
        numpy.testing.assert_array_equal(result, expected_result)
        
if __name__ == '__main__':
    unittest.main()