import unittest
import numpy

class TestArrayNegativeCopy(unittest.TestCase):
    def test_negative(self):
        test_input = [-1, -2, 5, 3]
        expected_result = [1, 2, -5, -3]
        
        result = numpy.negative(test_input)
        numpy.testing.assert_array_equal(result, expected_result)
        
if __name__ == '__main__':
    unittest.main()