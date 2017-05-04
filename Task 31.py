amount_of_symbls = int(input('Сколько букв вы хотите видеть в вашем пароле? ( Должно быть минимум 3 буквы) :'))
amount_of_numbers = int(input('Сколько цифр вы хотите видеть в вашем пароле? :'))
import unittest
def create_password(request_amount_symbl,request_amount_numbers):
    import random
    up_symls = 'Q,W,E,R,T,Y,U,I,O,P,A,S,D,F,G,H,J,K,L,Z,X,C,V,B,N,M'
    up_symls_list = up_symls.split(',')
    l_symls = 'm,q,w,e,r,t,y,u,i,o,p,a,s,d,f,g,h,j,k,l,z,x,c,v,b,n,m'
    l_symls_list = l_symls.split(',')
    numbers = '1,2,3,4,5,6,7,8,9,0'
    numbers_list = numbers.split(',')
    random_symbl = []
    for index in range(0,request_amount_symbl//2):
        if request_amount_symbl % 2 != 0:
            request_amount_symbl += 1
        random_index = random.randint(0,len(up_symls_list)-1)
        random_symbl.append(up_symls_list[random_index] )
    for index in range(0,request_amount_symbl//2):
        if request_amount_symbl %2 != 0:
            request_amount_symbl -= 1
        random_index = random.randint(0,len(l_symls_list)-1)
        random_symbl.append(l_symls_list[random_index] )
    for index in range(0, request_amount_numbers):
        random_index_number = random.randint(0, len(numbers_list) - 1)
        random_symbl.append(numbers_list[random_index_number])
    random.shuffle(random_symbl)
    password_string = ''.join(random_symbl)
    return password_string
print('Ваш пароль : ' , create_password(amount_of_symbls,amount_of_numbers))


class TestAmountOfSymbls(unittest.TestCase):
    def test_amount_of_symbl(self):
        enter_amount_of_s_and_n = create_password(amount_of_symbls,amount_of_numbers)
        self.assertEqual(len(enter_amount_of_s_and_n),amount_of_numbers + amount_of_symbls)
if __name__ =='__main__':
    unittest.main()




"""amount_of_symbls = int(input('Сколько букв вы хотите видеть в вашем пароле? :'))
amount_of_numbers = int(input('Сколько цифр вы хотите видеть в вашем пароле? :'))
import unittest
def create_password(request_amount_symbl,request_amount_numbers):
    import random
    symls = 'Q,W,E,R,T,Y,U,I,O,P,A,S,D,F,G,H,J,K,L,Z,X,C,V,B,N,M,m,q,w,e,r,t,y,u,i,o,p,a,s,d,f,g,h,j,k,l,z,x,c,v,b,n,m'
    symls_list = symls.split(',')
    numbers = '1,2,3,4,5,6,7,8,9,0'
    numbers_list = numbers.split(',')
    random_symbl = []
    for index in range(0,request_amount_symbl):
        random_index = random.randint(0,len(symls_list)-1)
        random_symbl.append(symls_list[random_index] )
    for index in range(0, request_amount_numbers):
        random_index_number = random.randint(0, len(numbers_list) - 1)
        random_symbl.append(numbers_list[random_index_number])
    random.shuffle(random_symbl)
    password_string = ''.join(random_symbl)
    return password_string
print('Ваш пароль : ' , create_password(amount_of_symbls,amount_of_numbers))


class TestAmountOfSymbls(unittest.TestCase):
    def test_amount_of_symbl(self):
        enter_amount_of_s_and_n = create_password(amount_of_symbls,amount_of_numbers)
        self.assertEqual(len(enter_amount_of_s_and_n),amount_of_numbers + amount_of_symbls)
if __name__ =='__main__':
    unittest.main()"""

