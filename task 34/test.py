import godzila
import person
import random
import unittest
import main

class TestGodzila(unittest.TestCase):
    def is_full(self):
        godzila_1 = godzila.Godzila(100)
        man_1 = person.Man(10, 90)
        self.fail(man_1.eating_people(godzila_1,man_1))
    def is_90_persent(self):
        godzila_1 = godzila.Godzila(100)
        self.assertEqual(godzila_1.stomach_limit,90)

if __name__=='__main__':
    unittest.main()



