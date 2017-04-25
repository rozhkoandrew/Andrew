# ПЕРВЫЙ СПОСОБ
def find_integers(numbers):
    for x in range(2,numbers+1):
        a = True
        for y in range(2,x):
            if x%y==0:
                a = False
                break
        if a == True:
            print(x)
find_integers(100)

# ВТОРОЙ СПОСОБ Более быстрый.
from math import sqrt
def is_integer(numbers):
    list_of_integers = []
    count_multipliers = 0
    for x in range(2,numbers+1):
        for y in range(2,x):
            if y > int((sqrt(x)) + 1): # для скорости работы программы
                break
            if x%y==0:
                count_multipliers = count_multipliers + 1
                break
            else:
                count_multipliers = 0
        if count_multipliers == 0 :
            list_of_integers.append(x)
    print(list_of_integers)
is_integer(100)


# Второе задание

import random

def random_integer(number):
    max_number = 0
    count_integers = 0
    a = number
    for x in range(2,number):
        if x > int((sqrt(number)) + 1):
            break
        if number%x==0:
            count_integers = count_integers + 1
    if count_integers > 0:
        number = number + 1
        random_integer(number)
    if count_integers == 0:
        print('Random integer : ', number)
        number = str(number)
        for y in number:
            if int(y) > int(max_number):
                max_number = int(y)
        print("max-number in random integer : ", max_number)
random_number = random.randint(100000000000,900000000000)
random_integer(random_number)


# 3е задание
choise = int(input(''))































