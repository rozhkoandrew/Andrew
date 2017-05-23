import godzila
import person
import random


def eating_people(godzila_1,man):
    if godzila.Godzila.is_godzila_full(godzila_1,man) == True:
        godzila.Godzila.people_eating(godzila_1,man)
    elif godzila.Godzila.is_godzila_full(godzila_1,man) == False:
        print('Godzila cannot eat so much, whe will be full ')




if __name__ == '__main__':
    amount_of_people = int(input('Enter amount of people for Godzila: '))
    godzila_1 = godzila.Godzila(1000)
    man_1 = person.Man(10,90)
    for man in range(1, amount_of_people):
        man = person.Man(random.randint(1, 200), random.randint(1, 100))
        (eating_people(godzila_1,man))
    #unittest.main()













