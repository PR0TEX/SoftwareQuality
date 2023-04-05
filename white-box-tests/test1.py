import unittest
import numpy

class Test(unittest.TestCase):
    
    def test(self):
        array = numpy.random.rand(5,6)
        
        reshaped_array = numpy.reshape(array, (4,3))
        
        
if __name__ == '__main__':
    unittest.main()