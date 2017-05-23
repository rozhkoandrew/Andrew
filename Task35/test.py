import point
import cercle
import unittest

class TrstIsPointInside(unittest.TestCase):
    def test_is_inside(self):
        point_1 = point.Point(0)
        cercle_1 = cercle.Cercle(10,4)
        self.assertEqual(cercle_1.is_inside(point_1.cordinate, cercle_1.cordinate, cercle_1.radius),True)

    def test_is_outside(self):
        point_1 = point.Point(0)
        cercle_1 = cercle.Cercle(4, 10)
        self.assertEqual(cercle_1.is_inside(point_1.cordinate, cercle_1.cordinate, cercle_1.radius), False)


if __name__=='__main__':
    unittest.main()