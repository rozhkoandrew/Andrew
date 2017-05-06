import unittest
import string
def create_password(request_amount_symbl,request_amount_numbers):
    import random
    random_symbol = []
    num_upper = request_amount_symbl // 2
    num_lower = request_amount_symbl - num_upper
    for index in range(0,num_upper):
        random_index = random.randint(0,len(string.ascii_uppercase)-1)
        random_symbol.append(string.ascii_uppercase[random_index] )
    for index in range(0,num_lower):
        random_index = random.randint(0,len(string.ascii_lowercase)-1)
        random_symbol.append(string.ascii_lowercase[random_index] )
    for index in range(0, request_amount_numbers):
        random_index_number = random.randint(0, len(string.digits) - 1)
        random_symbol.append(string.digits[random_index_number])
    random.shuffle(random_symbol)
    password_string = ''.join(random_symbol)
    return password_string
class TestAmountOfSymbls(unittest.TestCase):
    def test_isupper_symbols_inside(self):
        password = create_password(amount_of_symbols, amount_of_numbers)
        total_uppers = sum([1 for c in password if c in string.ascii_uppercase])
        self.assertTrue(total_uppers > 0)
    def test_islower_symbols_inside(self):
        password = create_password(amount_of_symbols,amount_of_numbers)
        total_lowers = sum([1 for low_str in password if low_str in string.ascii_lowercase])
        self.assertTrue(total_lowers>0)
    def  test_isnumbers_inside(self):
        password = create_password(amount_of_symbols,amount_of_numbers)
        total_numbers = sum([1 for number in password if number in string.digits])
        self.assertTrue((total_numbers > 0))
if __name__ =='__main__':
    amount_of_symbols = int(input('Сколько букв вы хотите видеть в вашем пароле? ( Должно быть минимум 2 буквы) :'))
    amount_of_numbers = int(input('Сколько цифр вы хотите видеть в вашем пароле?( Должна быть минимум 1 цифра) :'))
    print('Ваш пароль : ', create_password(amount_of_symbols, amount_of_numbers))
unittest.main()














