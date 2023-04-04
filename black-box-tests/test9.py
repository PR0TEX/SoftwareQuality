import unittest
import numpy

class TestLog(unittest.TestCase):
    def test_log(self):
        test_input = numpy.e
        expected_result = 1
        
        result = numpy.log(test_input)
        self.assertEqual(result, expected_result)
        
if __name__ == '__main__':
    unittest.main()