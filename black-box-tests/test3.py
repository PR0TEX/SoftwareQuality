import unittest
import numpy

class TestSinCorrectness(unittest.TestCase):
    def test_sin(self):
        test_input = numpy.pi/2
        expected_result = 1
        
        result = numpy.sin(test_input)
        self.assertEqual(result, expected_result)
        
if __name__ == '__main__':
    unittest.main()