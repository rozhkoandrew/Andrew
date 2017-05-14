import random

first_lst = [x for x in range(2,10)]
second_lst = [x for x in range(2,10)]
final_lst = []

def make_multily(number_1,number_2):
    mult = ('%s * %s'%(number_2,number_1))
    return mult

def take_numbers_from_list(first_lst,second_lst):
    lst_1 = []
    x = 0
    while x !=15:
        a = random.choice(first_lst)
        b = random.choice(second_lst)
        if make_multily(a,b) in lst_1:
            continue
        elif make_multily(b,a) in lst_1:
            continue
        else:
            lst_1.append(make_multily(a,b))

        x+=1
    return lst_1
print(take_numbers_from_list(first_lst,second_lst))


