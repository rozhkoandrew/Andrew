##################TASK - 25###################
lst_of_numbers = [1,2,3,4,5,6,7,8,9,10]
def average_number(lst_of_numbers):
    sum_of_numbers = 0
    for index,number in enumerate(lst_of_numbers):
        index += 1
        sum_of_numbers +=number
    lst_of_numbers = sum_of_numbers/index
    return  lst_of_numbers
print(average_number(lst_of_numbers))

##################TASK - 26###################
def count_odd2even(lst_of_numbers,):
    odd = 0
    even = 0
    result = 0
    for x in lst_of_numbers:
        if x % 2 == 0:
            even += x
        elif x % 2 != 0:
            odd += x
    result = even - odd
    return result
print(count_odd2even(lst_of_numbers))

##################TASK - 27###################

import random
odd_numbers = []
cheking = 0
for odd_nuber in range(1,100):
    if odd_nuber % 2 != 0:
        odd_numbers.append(odd_nuber)
print(odd_numbers)
lst_lenth = len(odd_numbers)-1
a = random.randint(1,lst_lenth)
for index,number in enumerate(odd_numbers):
    print(index,number)


print((odd_numbers))





"""import random
odd_numbers = []
for odd_nuber in range(1,100):
    if odd_nuber % 2 != 0:
        odd_numbers.append(odd_nuber)
print(odd_numbers)
lst_lenth = len(odd_numbers)-1
for index,number in enumerate(odd_numbers):
    odd_numbers[random.randint(1,lst_lenth)] = number
print((odd_numbers))"""

##################TASK - 28###################
def first_or_second_lst (low_limit,upper_limit):
    first_lst = []
    second_lst = []
    for x in range(low_limit,upper_limit+1):
        first_lst.append(random.randint(low_limit,upper_limit))
        second_lst.append(random.randint(low_limit, upper_limit))
    print(first_lst)
    print(second_lst)
    print(average_number(first_lst))
    print(average_number(second_lst))
    if average_number(first_lst) > average_number(second_lst):
        print('First list everage number bigger')
    elif average_number(first_lst)<average_number(second_lst):
        print('Second list everage number bigger')
    else:
        print('They are quqal')
first_or_second_lst(0,5)

##################TASK - 29###################
def where_is_bigger_amount_of_number(amount_of_numbers,lower_limit,upper_limit):
    lst = []
    for x in range(1,amount_of_numbers):
        lst.append(random.randint(lower_limit,upper_limit))
    print(len(lst))
    print(lst)
    zero = 0
    minus_one = 0
    one = 0
    for x in lst:
        if x == 0:
            zero += 1
        elif x == -1:
            minus_one += 1
        elif x == 1:
            one+=1
    if zero > one and  zero >  minus_one :
        print(" Most numbers in list it is 0  ")
    if minus_one > zero and minus_one >one :
        print(" Most numbers in list it is -1  ")
    if one > zero and  one > minus_one :
        print(" Most numbers in list it is 1  ")
where_is_bigger_amount_of_number(12,-1,1)


##################TASK - 30####################
string_entering = input('Введите имя в нижнем регистре на русском языкеан: ')
def cripto_cod(string):
    cripto_cod = 'йцукенгшщзхъфыва-пролджэячсмитьбю1234567890'
    #string_entering = input('Пожалуйста, введите имя ')
    #string_entering = 'йцукен09'
    index_num_str = []
    result = []
    final = ''
    #index_distance = len(cripto_cod) - index_1
    for index , symbl in enumerate(string_entering):
        for index_1,symbl_1 in enumerate(cripto_cod):
            if symbl == symbl_1:
                index_1 += 5
                if index_1 > len(cripto_cod):
                    #index_1 = 0
                    index_1 -= len(cripto_cod)
                result.append(index_1)
                count_index = index_1
                final += cripto_cod[count_index]
    print('Ваше Имя в зашифрованном виде : ', final)


cripto_cod(string_entering)































