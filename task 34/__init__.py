import Dodzila
import People
import random
import unittest

def eating_people(man):
    if Dodzila.Godzila.is_godzila_full(godzila,man) == True:
        Dodzila.Godzila.people_eating(godzila,man)
    elif Dodzila.Godzila.is_godzila_full(godzila,man) == False:
        print('Godzila cannot eat so much, whe will be full ')


if __name__ == '__main__':
    amount_of_people = int(input('Enter amount of people for Godzila: '))
    godzila = Dodzila.Godzila(1000)
    man_1 = People.People(10,90)
    for man in range(1, amount_of_people):
        man = People.People(random.randint(1, 200), random.randint(1, 100))
        (eating_people(man))













