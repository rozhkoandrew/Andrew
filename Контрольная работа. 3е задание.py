import unittest
import random
def create_fibinachi_lst(amount_of_numbers):
    fibonachi_lst = [1, 1, 2]
    for x in range(3, amount_of_numbers):
        fibonachi_lst.append(fibonachi_lst[x - 1] + fibonachi_lst[x - 2])
    return fibonachi_lst
def find_sum_fibonachi_list(amount_of_numbers):
    fibonachi_list = create_fibinachi_lst(amount_of_numbers)
    return sum(fibonachi_list)
class TestFibonachiList(unittest.TestCase):
    def test_isfibonachi_numbers_inside(self):
        sum_fibonachi = find_sum_fibonachi_list(10)
        self.assertEquals = (sum_fibonachi, 143)
def change_max_and_min(lst):
    max_value = max(lst)
    min_value = min(lst)
    for x in range(0, len(lst)):
        if lst[x] == max_value:
            lst[x] = min_value
            continue
        if lst[x] == min_value:
            lst[x] = max_value
            continue
    return lst
class TestisChangeMaxandMin(unittest.TestCase):
    def test_is_reverse_max_min(self):
        lst = change_max_and_min(create_fibinachi_lst(10))
        max_value_index = lst.index(max(lst))
        min_value_index = lst.index(min(lst))
        self.assertTrue(max_value_index == 0)
        self.assertTrue(min_value_index == 9)

def normalize_lst(lst):
    abs_max = max([abs(x) for x in lst])
    persent_list = [lst[x] / abs_max for x in range(0, len(lst))]
    return persent_list
class TestIsNormilizeTo1(unittest.TestCase):
    def test_is_normilize_to_1(self):
        check_list = []
        lst = [1, 3, 4, 5, 6, -4, 0, -0, -3]
        for x in normalize_lst(lst):
            if x >1 or x < -1 :
                break
            else:
                check_list.append(x)
        self.assertEqual(len(check_list) , len(lst))
if __name__ == "__main__":
    print(find_sum_fibonachi_list(10))
    print(change_max_and_min(create_fibinachi_lst(10)))
    print(normalize_lst([x for x in range(-6, 7)]))
    unittest.main()









