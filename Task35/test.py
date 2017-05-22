import point
import cercle
import unittest

class TrstIsPointInside(unittest.TestCase):
    def test_is_inside(self):
        point_1 = point.Point(20, 5)
        cercle_1 = cercle.Cercle(20, 20, 4)
        self.assertEqual(cercle_1.is_inside(point_1.coordinates, cercle_1.center_cordinate, cercle_1.radius),True)

    def test_is_outside(self):
        point_1 = point.Point(20, 40)
        cercle_1 = cercle.Cercle(20, 20, 4)
        self.assertEqual(cercle_1.is_inside(point_1.coordinates, cercle_1.center_cordinate, cercle_1.radius), False)


if __name__=='__main__':
    unittest.main()