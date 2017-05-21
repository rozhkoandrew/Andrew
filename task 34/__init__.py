import Dodzila
import People
import random
import unittest

def eating_people(godzila,man):
    if Dodzila.Godzila.is_godzila_full(godzila,man) == True:
        Dodzila.Godzila.people_eating(godzila,man)
    elif Dodzila.Godzila.is_godzila_full(godzila,man) == False:
        print('Godzila cannot eat so much, whe will be full ')


class TestGodzila(unittest.TestCase):
    def is_full(self):
        godzila_1 = Dodzila.Godzila(100)
        man_1 = People.Man(10, 90)
        self.fail(eating_people(godzila_1,man_1))
    def is_90_persent(self):
        godzila = Dodzila.Godzila(100)
        self.assertEqual(godzila.stomach_limit,90)

if __name__ == '__main__':
    amount_of_people = int(input('Enter amount of people for Godzila: '))
    godzila = Dodzila.Godzila(1000)
    man_1 = People.Man(10,90)
    for man in range(1, amount_of_people):
        man = People.Man(random.randint(1, 200), random.randint(1, 100))
        (eating_people(godzila,man))
    unittest.main()













