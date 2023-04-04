import unittest
import numpy

class TestCosCorrectness(unittest.TestCase):
    def test_cos(self):
        test_input = numpy.pi/3
        expected_result = 0.5
        
        result = numpy.cos(test_input)
        self.assertEqual(numpy.round(result,2), expected_result)
        
if __name__ == '__main__':
    unittest.main()