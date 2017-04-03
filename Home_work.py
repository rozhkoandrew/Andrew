print(' Task # 1') #Task 1
# Найти результат выражения для произвольных значений a,b,c: a + b * ( c / 2 )
a = 5
b = 7 #Objects
c = 3
result_ab = a + b
c_devisions = c / 2 # acts
if c != 0:
    final_result = result_ab * c_devisions
    print(" We have 3 objects  a = %d, b = %d, c = %d. Result of a + b = %d, Result of c / 2 = %.2f"
         "    \nAnd final multiplicate = %.2f " % (a,b,c,result_ab,c_devisions,final_result )) #Final
elif c == 0:
    print(" ZeroDevisionError")

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
division = a_add_b / 12
if division != 0:
    c_mult = division * c # acts
    div_dif = c_mult % 4
    add_b = div_dif + b
else:
    print(" ZeroDevisionError")
print(" Now we again have 3 objects. a= %d, b= %d, and c= %d. \nPrimirly we will add a and b "
      "and receive - %d, \nAfter this we will divide this number on 12 and receive - %.2f. "
      "\n now if resuld not 0 we will multiplicate  this number on c and receive - %.2f."
      "\n Division diference on 4 will be - %d. And if we will add b - we will have final "
      "nubmer - %d  " % (a,b,c, a_add_b, division, c_mult, div_dif, add_b))


print(' Task # 3') #Task 3
# Найти результат выражения для произвольных значений a,b,c: (a - b * c ) / ( a + b ) % c
a = 1001
b = 4002
c = 7800
first_act = b * c
first_act = first_act - a
second_act = a + b
division = first_act / second_act
if division != 0:
    final = division % c
elif division == 0:
    print(" ZerroDivisioError")
print(" 3 objects a= %d, b= %d, c= %d. \nFirst of all we will multiplicate b on c , and take away c"
      "we will receive - %d. \n after this we will add a to b and receise - %d "
      "\nNow divide this two objects  and receive - %2.f. "
      "\nAnd lets look for division fission residue - %d" %(a,b,c, first_act,second_act,division,final))











