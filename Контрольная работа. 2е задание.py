import unittest
import random
def sum_odd_numbers(number):
    list_of_odd_numbers = []
    string = str(number)
    for x in range(0,len(string)):
        if int(string[x])% 2 !=0:
            list_of_odd_numbers.append(int(string[x]))
    return sum(list_of_odd_numbers)

class TestIsReturnSummOfOddNumbers(unittest.TestCase):
    def test_is_return_sumOfodd(self):
        result = sum_odd_numbers(12345)
        self.assertEqual(result,9)



def which_number_is_closer_to_10(number_1,number_2):
    import math
    checking_1 =  math.fabs(number_1- 10)
    checking_2 = math.fabs(number_2 - 10)
    if checking_1 < checking_2:
        return number_1
    elif checking_1 > checking_2:
        return number_2

class TestDistanseTo10(unittest.TestCase):
    def test_where_less_distanse(self):
        less_distance = which_number_is_closer_to_10(9.1, 11)
        self.assertEqual(less_distance, 9.1)




def find_primes(numbers):
    primes = []
    for x in range(2,numbers+1):
        is_prime = True
        for y in range(2,x):
            if x%y==0:
                is_prime = False
                break
        if is_prime == True:
            primes.append(x)
    random.shuffle(primes)
    return primes
list_of_primes = find_primes(100)
def fill_lst_with_random_integers(numbers):
    for x in range(0, len(numbers)):
        numbers[x] = list_of_primes[x]
    return numbers
class TestIsInteger(unittest.TestCase):
    def test_is_integers_inside(self):
        list_1 = fill_lst_with_random_integers(lst)
        deviders = []
        for x in list_1:
            if x in list_of_primes:
                deviders.append(x)
            else:
                break
        self.assertEqual(len(lst),len(deviders))



if __name__=='__main__':
    enter_number = int(input('Введите число'))
    print(sum_odd_numbers(enter_number))
    first_number = float(input('Введите первое число: '))
    second_number = float(input('Введите второе числ: '))
    print(which_number_is_closer_to_10(first_number, second_number))
    lst = [12, 14.6, 'vdvd', True, 23, [2,4,5], 7, 3, 9, 10]
    print(fill_lst_with_random_integers(lst))
    unittest.main()

""" import unittest
import random


def sum_odd_numbers(number):
    list_of_odd_numbers = []
    string = str(number)
    for x in range(0, len(string)):
        if int(string[x]) % 2 != 0:
            list_of_odd_numbers.append(int(string[x]))
    return sum(list_of_odd_numbers)


class TestIsReturnSummOfOddNumbers(unittest.TestCase):
    def test_is_return_sumOfodd(self):
        result = sum_odd_numbers(12345)
        self.assertEqual(result, 9)


if __name__ == '__main__':
    enter_number = int(input('Введите число'))
    print(sum_odd_numbers(enter_number))
    unittest.main()


def which_number_is_closer_to_10(number_1, number_2):
    import math
    checking_1 = math.fabs(number_1 - 10)
    checking_2 = math.fabs(number_2 - 10)
    if checking_1 < checking_2:
        return number_1
    elif checking_1 > checking_2:
        return number_2
    else:
        return None


class TestDistanseTo10(unittest.TestCase):
    def test_where_less_distanse(self):
        less_distance = which_number_is_closer_to_10(9.1, 11)
        self.assertEqual(less_distance, 9.1)

    def test_if_equal_distance(self):
        equal_distance_number = which_number_is_closer_to_10(9.1, 10.9)
        self.assertEqual(equal_distance_number, None)


if __name__ == '__main__':
    first_number = float(input('Введите первое число: '))
    second_number = float(input('Введите второе числ: '))
    print(which_number_is_closer_to_10(first_number, second_number))
    unittest.main()


def find_integers(numbers):
    integers = []
    for x in range(2, numbers + 1):
        is_prime = True
        for y in range(2, x):
            if x % y == 0:
                is_prime = False
                break
        if is_prime == True:
            integers.append(x)
    return integers


def fill_lst_with_random_integers(numbers):
    for x in range(0, len(numbers)):
        random_index = random.randint(0, len(find_integers(100)) - 1)
        y = numbers[x]
        numbers[x] = find_integers(100)[random_index]
        find_integers(100)[random_index] = y
    return numbers


class TestIsInteger(unittest.TestCase):
    def test_is_integers_inside(self):
        list_1 = fill_lst_with_random_integers(lst)
        deviders = []
        for x in fill_lst_with_random_integers(lst):
            is_prime = True
            for y in range(2, (x - 1)):
                if x % y == 0:
                    is_prime = False
                    break
            if is_prime == True:
                deviders.append(x)
        self.assertEqual(len(lst), len(deviders))


if __name__ == '__main__':
    find_integers(100)
    lst = [12, 14.6, 'vdvd', True, 23, [2, 4, 5], 7, 3, 9, 10]
    print(fill_lst_with_random_integers(lst))
    unittest.main()
"""

















