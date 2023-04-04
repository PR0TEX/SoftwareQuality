import unittest
import numpy

class TestLog10(unittest.TestCase):
    def test_log10(self):
        test_input = 100
        expected_result = 2
        
        result = numpy.log10(test_input)
        self.assertEqual(result, expected_result)
        
if __name__ == '__main__':
    unittest.main()