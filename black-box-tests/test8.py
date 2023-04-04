import unittest
import numpy

class TestLog2(unittest.TestCase):
    def test_log2(self):
        test_input = 8
        expected_result = 3
        
        result = numpy.log2(test_input)
        self.assertEqual(result, expected_result)
        
if __name__ == '__main__':
    unittest.main()