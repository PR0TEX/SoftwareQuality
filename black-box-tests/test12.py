import unittest
import numpy

class TestArrayCopy(unittest.TestCase):
    def test_positive(self):
        test_input = [-1, -2, 5, 3]
        expected_result = [-1, -2, 5, 3]
        
        result = numpy.positive(test_input)
        numpy.testing.assert_array_equal(result, expected_result)
        
if __name__ == '__main__':
    unittest.main()