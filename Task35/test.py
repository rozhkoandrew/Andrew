import point
import cercle
import unittest

class TrstIsPointInside(unittest.TestCase):
    def test_is_inside(self):
        point_1 = point.Point(0, 0)
        cercle_piont = point.Point(1, 1)
        cercle_1 = cercle.Cercle(cercle_piont, 4)
        self.assertEqual(cercle_1.is_inside(point_1.x, point_1.y, cercle_piont.x, cercle_piont.y, cercle_1.radius), True)

    def test_is_outside(self):
        point_1 = point.Point(0, 0)
        cercle_piont = point.Point(10, 10)
        cercle_1 = cercle.Cercle(cercle_piont, 4)
        self.assertEqual(cercle_1.is_inside(point_1.x,point_1.y,cercle_piont.x,cercle_piont.y ,cercle_1.radius), False)


if __name__=='__main__':
    unittest.main()