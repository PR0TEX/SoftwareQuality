import unittest
import numpy

class TestArraySum(unittest.TestCase):
    def test_array_sum(self):
        test_input = [0.5, 1.5, 2.0, 1.5]
        expected_result = 5.5
        
        result = numpy.sum(test_input)
        self.assertEqual(result, expected_result)
        
if __name__ == '__main__':
    unittest.main()