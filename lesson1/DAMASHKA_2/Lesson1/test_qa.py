import unittest
from simple_math import SimpleMath

class TestSimpleMath(unittest.TestCase):
    def setUp(self):
        # ეს ქმნის SimpleMath კლასის ეგზემპლარს ტესტებისთვის
        self.math = SimpleMath()

    def test_square(self):
        self.assertEqual(self.math.square(2), 4)
        self.assertEqual(self.math.square(-3), 9)
        self.assertEqual(self.math.square(0), 0)

    def test_cube(self):
        self.assertEqual(self.math.cube(2), 8)
        self.assertEqual(self.math.cube(-3), -27)
        self.assertEqual(self.math.cube(0), 0)

if __name__ == '__main__':
    unittest.main()