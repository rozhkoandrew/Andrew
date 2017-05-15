import random
import unittest
first_lst = [x for x in range(2,10)]
second_lst = [x for x in range(2,10)]
amount_of_multipliers = 15
def make_multily(number_1,number_2):
    mult = ('%s * %s'%(number_2,number_1))
    return mult
def take_numbers_from_list(first_lst,second_lst):
    lst_1 = []
    x = 0
    while x !=amount_of_multipliers:
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
class TestMultiplyExamples(unittest.TestCase):
    def test_is_not_repeats_itself(self):
        check_lst = []
        first_lst = [x for x in range(2, 10)]
        second_lst = [x for x in range(2, 10)]
        result = take_numbers_from_list(first_lst,second_lst)
        for x in result:
            if x in check_lst:
                break
            elif x[::-1] in check_lst:
                break
            else:
                # print(x[::-1],x)
                check_lst.append(x)
        self.assertTrue(len(check_lst) == amount_of_multipliers)

if __name__ =='__main__':
    print(take_numbers_from_list(first_lst, second_lst))
    unittest.main()


