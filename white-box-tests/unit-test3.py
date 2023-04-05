import unittest
from numpy.linalg import *
from numpy.testing import assert_array_equal

class Test(unittest.TestCase):
    def test(self):
        A = ([[1, 2, 1], [2, 1, 2], [1, 2, 1]])
        expected_result = [[6, 6, 6], [6, 9, 6], [6, 6, 6]]

        assert assert_array_equal(matrix_power(A, 2), expected_result)


if __name__ == '__main__':
    unittest.main()