#########ПЕРВЫЙ СПОСОБ с булеоном###### ###### ###### ###### ###### ######
def find_integers(numbers):
    for x in range(2,numbers+1):
        is_prime = True
        for y in range(2,x):
            if x%y==0:
                is_prime = False
                break
        if is_prime == True:
            print(x)
find_integers(100)
#########ВТОРОЙ СПОСОБ с подсчетом делителей###### ###### ######
from math import sqrt
def find_integers(numbers):
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
find_integers(100)
######### Объединение первого и второго способа #########
def find_integers(numbers):
    list_of_integers = []
    for x in range(2,numbers+1):
        is_prime = True # Задать вопрос.
        for y in range(2, int((sqrt(x))) + 1):
            if x%y==0:
                is_prime = False
                break
        if is_prime == True:
            list_of_integers.append(x)
    return list_of_integers
print(find_integers(100))


# ############### ###### ###### ###### Второе задание ############### ###### ######

import random

def max_value_of_random_number(number):
    print('Random number: ', number)
    max_number = 0
    number = str(number)
    for y in number:
        if int(y) > int(max_number):
            max_number = int(y)
    print("max-number in random integer : ", max_number)
random_number = random.randint(int(1e11), int(1e12-1)) # e = 10**2
max_value_of_random_number(random_number)

###### ###### Определение простого числа из рандомного и его максимальное значение.######  ######
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
random_number = random.randint(int(1e11), int(1e12-1)) #e = 10**2
random_integer(random_number)


####### ###### ######  5е задание ###### ###### ###### ###### ######



def factorial_by_recursion(number):
    if number == 0:
        return 1
    else:
        return number * factorial_by_recursion(number - 1)

print(factorial_by_recursion(5))



import random
####### ###### ######  4е задание ###### ###### ###### ###### ######
answer = int(random.randint(1,10))
did_gues = False
while did_gues  == False:
    choise = int(input('Guess a number from 1 to 10 '))
    if choise < answer:
        print('Cold, ansrew should number should be bigger ')
        did_gues = False
    elif choise > answer:
        print('Cold, should be less')
        did_gues = False
    elif choise == answer:
        print("Yeah, you right. Winner, congratulations. ")
        did_gues = True






































