import unittest
from numpy.matrixlib.defmatrix import *
from numpy.matlib import zeros
from numpy.testing import assert_array_equal

class Test(unittest.TestCase):
    def test_zeros():
        assert_array_equal(zeros((5, 3)),
                        matrix([[ 0.,  0.,  0.],
                                    [ 0.,  0.,  0.],
                                    [ 0.,  0.,  0.],
                                    [ 0.,  0.,  0.],
                                    [ 0.,  0.,  0.]]))

        assert_array_equal(zeros(3), matrix([[ 0.,  0.,  0.]]))
        
if __name__ == '__main__':
    unittest.main()