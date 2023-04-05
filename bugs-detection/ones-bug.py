import unittest
import numpy

class GenerateArrayWithLargeNumberOfFloatOnes(unittest.TestCase):
    def test(self):
        result = numpy.ones((200000000, 2), dtype=numpy.float32).mean(axis=0)
        expected_result = [1., 1.]
        
        numpy.testing.assert_array_equal(result, expected_result)
        
if __name__ == '__main__':
    unittest.main()