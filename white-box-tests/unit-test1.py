import unittest
from numpy.matrixlib.defmatrix import *
from numpy.matlib import empty
from numpy.testing import assert_

class Test(unittest.TestCase):
    def test_empty(self):
        x = empty((5,))
        assert_(isinstance(x, matrix))
        assert_(x.shape, (1, 5))
        
        
if __name__ == '__main__':
    unittest.main()