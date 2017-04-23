"""def unicode_symbl(unicode_1, unicode_2):
    sum_of_unicode = 0
    if ord(unicode_2) > ord(unicode_1):
        for unicode_symbl in range (ord(unicode_1), ord(unicode_2)+1):
            sum_of_unicode = sum_of_unicode + unicode_symbl
        return sum_of_unicode
    elif ord(unicode_1) > ord(unicode_2):
        for unicode_symbl in range (ord(unicode_2), ord(unicode_1)+1):
            sum_of_unicode = sum_of_unicode + unicode_symbl
        return sum_of_unicode
print(unicode_symbl('a','d')) """

def unicode_symbl(unicode_1, unicode_2):
    sum_of_unicode = 0
    max_char = max(ord(unicode_1), ord(unicode_2))
    min_char = min(ord(unicode_1), ord(unicode_2))
    for char in range(min_char, max_char+1):
        sum_of_unicode = sum_of_unicode + char
    return sum_of_unicode
print(unicode_symbl('a','d'))



def power_sum_counting(number):
    x=0
    summ_power = 0
    while number**x<= 1000:
        num = 3**x
        summ_power = summ_power + num
        x = x + 1
    return summ_power
print(power_sum_counting(3))


def num_finder(*numbers):
    for numbers in range(0,1001):
        string = str(numbers)
        if '1' in string and '7' in string:
            print(numbers)
num_finder(1,7)





















