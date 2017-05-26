import point
import circle
import unittest

class TrstIsPointInside(unittest.TestCase):
    def test_is_inside(self):
        point_1 = point.Point(0, 0)
        circle_1 = circle.Circle(1, 1, 4)
        self.assertEqual(circle_1.is_inside(point_1), True)

    def test_is_outside(self):
        point_1 = point.Point(0, 0)
        circle_1 = circle.Circle(10, 10, 4)
        self.assertEqual(circle_1.is_inside(point_1), False)


if __name__=='__main__':
    unittest.main()