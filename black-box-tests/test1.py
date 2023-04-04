import unittest
import numpy

class TestRoundTwoDecimalPlaces(unittest.TestCase):
    def test_round_two_decimal_places(self):
        test_input = 100.123
        expected_result = 100.12
        
        result = numpy.around(test_input,2)
        self.assertEqual(result, expected_result)
        
if __name__ == '__main__':
    unittest.main()