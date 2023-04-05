import unittest
import numpy
# 1e-18 = 1 * 10^-18
# 1e-18j = 1 * 10^-18 * sqrt(-1)
class TestAccurationOfLog1pForSmallComplexInput(unittest.TestCase):
    def test(self):
        result = numpy.log1p(1e-18 + 1e-18j)
        expected_result = 1e-18 + 1e-18j 
        
        self.assertEqual(result, expected_result)
        
if __name__ == '__main__':
    unittest.main()