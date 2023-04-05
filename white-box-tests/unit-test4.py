import numpy.random
import unittest


class TestRandom(unittest.TestCase):
    def test_random(self):
        s = numpy.random.RandomState(0)
        self.assertEqual(s.randint(1000), 684)
        s = numpy.random.RandomState(4294967295)
        self.assertEqual(s.randint(1000), 419)


if __name__ == '__main__':
    unittest.main()