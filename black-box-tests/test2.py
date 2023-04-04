import unittest
import numpy

class TestRoundTwoDecimalPlaces(unittest.TestCase):
    def test_floor_rounding(self):
        test_input = 100.54
        expected_result = 100
        
        result = numpy.floor(test_input)
        self.assertEqual(result, expected_result)
        
if __name__ == '__main__':
    unittest.main()