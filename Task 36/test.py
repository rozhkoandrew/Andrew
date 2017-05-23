import vehicle
import train
import airplane
import unittest

class TestVehicles(unittest.TestCase):
    def test_is_add_carrige(self):
        train_1 = train.Train('V-342', 80, 8, 60, 15)
        train_1.print_info()
        train_1.add_carriage_or_reduce(+2)
        train_1.print_info()
        self.assertEqual(train_1.carriage_n,17)

    def test_is_ruduce_carrige(self):
        train_1 = train.Train('V-342', 80, 8, 60, 15)
        train_1.print_info()
        train_1.add_carriage_or_reduce(-2)
        train_1.print_info()
        self.assertEqual(train_1.carriage_n,13)

    def test_is_count_tarin_speed(self):
        train_1 = train.Train('V-342', 80, 8, 60, 15)
        train_1.print_info()
        train_1.add_carriage_or_reduce(+2)
        train_1.print_info()
        self.assertTrue(train_1.speed == 45)

    def test_baggage(self):
        airplane_1 = airplane.Airplane('Boing-747', 40, 12, 200, 300)
        airplane_1.print_info()
        self.assertEqual(airplane_1.bagage_capacity , 400)


if __name__=='__main__':
    unittest.main()