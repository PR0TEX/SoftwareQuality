import unittest
import numpy

class TestLog1p(unittest.TestCase):
    def test_log1p(self):
        test_input = 1e-99
        expected_result = 1e-99
        
        result = numpy.log1p(test_input)
        self.assertEqual(result, expected_result)
        
if __name__ == '__main__':
    unittest.main()