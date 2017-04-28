##################TASK - 25###################
lst_of_numbers = [1,2,3,4,5,6,7,8,9,10]
def everage_number(lst_of_numbers):
    sum_of_numbers = 0
    for index_1,number_1 in enumerate(lst_of_numbers):
        index_1 += 1
        sum_of_numbers +=number_1
    lst_of_numbers = sum_of_numbers/index_1
    return  lst_of_numbers
print(everage_number(lst_of_numbers))

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
for odd_nuber in range(1,100):
    if odd_nuber % 2 != 0:
        odd_numbers.append(odd_nuber)
print(odd_numbers)
lst_lenth = len(odd_numbers)-1
for index,number in enumerate(odd_numbers):
    odd_numbers[random.randint(1,lst_lenth)] = number
print((odd_numbers))

##################TASK - 28###################
first_lst = []
second_lst = []
for x in range(0,6):
    first_lst.append(random.randint(0,5))
    second_lst.append(random.randint(0, 5))
print(first_lst)
print(second_lst)
print(everage_number(first_lst))
print(everage_number(second_lst))
def first_or_second_lst (first_lst,second_lst):
    if everage_number(first_lst) > everage_number(second_lst):
        print('First list everage number bigger')
    elif everage_number(first_lst)<everage_number(second_lst):
        print('Second list everage number bigger')
    else:
        print('They are quqal')
first_or_second_lst(first_lst,second_lst)

##################TASK - 29###################

lst = []
for x in range(1,12):
    lst.append(random.randint(-1,1))
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
if zero > minus_one  and one:
    print(" Most numbers in list it is 0  ")
elif minus_one > zero and one:
    print(" Most numbers in list it is -1  ")
elif one > zero and minus_one:
    print(" Most numbers in list it is 1  ")
else:
    pass


##################TASK - 30####################
"""cripto_cod = 'йцукенгшщзхъфывапролджэячсмитьбю1234567890'
#string_entering = input('Пожалуйста, введите имя ')
string_entering = 'йцукен19'
index_num_str = []
result = []
count_index = []
for index , symbl in enumerate(string_entering):
    for index_1,symbl_1 in enumerate(cripto_cod):
        if symbl == symbl_1:
            index_1 += 5
            result.append(cripto_cod[index_1])
            

print('11-------',index_num_str)
print(result)
print(len(cripto_cod))"""



























