import unittest
import numpy

class TestNumberAddition(unittest.TestCase):
    def test_add_numbers(self):
        test_input_a = 5
        test_input_b = 7
        expected_result = 12
        
        result = numpy.add(test_input_a, test_input_b)
        self.assertEqual(result, expected_result)
        
if __name__ == '__main__':
    unittest.main()