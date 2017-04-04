print(' Task # 1') #Task 1
# Найти результат выражения для произвольных значений a,b,c: a + b * ( c / 2 )
a = 5
b = 7 #Objects
c = 3
result_ab = a + b
div_num =  2
if div_num != 0:
    c_devisions = c / div_num  # acts
elif div_num == 0:
    print(" ZeroDevisionError")
final_result = result_ab * c_devisions
print(" We have 3 objects  a = %d, b = %d, c = %d. Result of a + b = %d, Result of c / 2 = %.2f"
         "    \nAnd final multiplicate = %.2f " % (a,b,c,result_ab,c_devisions,final_result )) #Final


print(' Task # 2') #Task 2
# Найти результат выражения для произвольных значений a,b: (a2 + b2) % 2
a = 42
b = 84 #Objects
a_mult = a**2
b_mult = b**2
ab_add = a_mult+b_mult # acts
final_act = ab_add % 2
print(" Now we have only 2 objects a = %d, b = %d . Primirly we will elevate this numbers "
     " a will = %d , and b will = %d .\nIf we will add this numbers - we will receive %d"
     "  \nAnd division difference will be - %d  " % (a,b,a_mult,b_mult,ab_add,final_act))


print(' Task # 3') #Task 3
#Найти результат выражения для произвольных значений a,b,c: ( a + b ) / 12 * c % 4 + b
a = 101
b = 308 #Objects
c = 567
a_add_b = a+b
div_num = 12
if div_num != 0:
    division =  a_add_b / div_num
else:
    print(" ZeroDevisionError")
c_mult = division * c # acts
div_dif = c_mult % 4
add_b = div_dif + b
print(" Now we again have 3 objects. a= %d, b= %d, and c= %d. \nPrimirly we will add a and b "
      "and receive - %d, \nAfter this we will divide this number on 12 and receive - %.2f. "
      "\n now if resuld not 0 we will multiplicate  this number on c and receive - %.2f."
      "\n Division diference on 4 will be - %d. And if we will add b - we will have final "
      "nubmer - %d  " % (a,b,c, a_add_b, division, c_mult, div_dif, add_b))


print(' Task # 4') #Task 4
# Найти результат выражения для произвольных значений a,b,c: (a - b * c ) / ( a + b ) % c
a = 1001
b = 4002     #Objects
c = 7800
first_act = b * c
first_act = first_act - a
second_act = a + b   # acts
if second_act != 0:
    division = first_act / second_act
else:
    print('ZeroDevisionError')
final = division % c
print(" ZerroDivisioError")
print(" 3 objects a= %d, b= %d, c= %d. \nFirst of all we will multiplicate b on c , and take away c"
      "we will receive - %d. \n after this we will add a to b and receise - %d "
      "\nNow divide this two objects  and receive - %2.f. "
      "\nAnd lets look for division fission residue - %d" %(a,b,c, first_act,second_act,division,final))

print(' Task # 5') #Task 5
 #Найти результат выражения для произвольных значений a,b,c: | a - b | /( a + b)3 - cos( c )
import math
a = 10100.
b = 40500    #Objects
c = 500010
a_fabs = math.fabs(a - b)
add_ab = a + b
add_ab = add_ab**3    # acts
division =  a_fabs / add_ab
cos_c = math.cos(c)
final = division - cos_c
print(' We have a= %d, b= %d, c= %d.'
      '\nHere we receive module from a - b - %d.'
      '\nHere we add a and b, and elevate on 3 - %d '
      '\n Here we made division on previos number - %d'
      '\n Here we take cos from c - %.3f'
      '\n and here we have final result - %.3f ' % (a,b,c,a_fabs, add_ab,division,cos_c, final ))

print(' Task # 6') #Task 6
#Найти результат выражения для произвольных значений a,b,c: ( ln( 1 + c ) / -b )4+ | a |
import math
a = 142
b = -2
c =  459
d = 4
if c != - c:
    ad_c = 1 + c
elif c == -c:
    print('TypeError')
ln_c = math.log(ad_c)
division = b**d
if d % 2 == 0:
    b = 2
else:
    b = -2
division = ln_c / division
if division != 0:
    final = math.fabs(a) + division
elif division == 0:
    print('ZeroDivisionError')
print (' we have a= %d, b= %d, c= %d.'
       '\n add c and 1 = %d '
       '\n find log for this number - %.2f'
       '\n if log not 0 , divide this on -b evaluated on 4 = %.2f'
       '\n  a + preveous number = %.3f' %(a,b,c, ad_c, ln_c, division,final))
























