import unittest
import numpy

class TestTanCorrectness(unittest.TestCase):
    def test_tan(self):
        test_input = 0
        expected_result = 0
        
        result = numpy.tan(test_input)
        self.assertEqual(result, expected_result)
        
if __name__ == '__main__':
    unittest.main()