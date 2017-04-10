import math
def degres2radians(degres):
    degres2radians = (degres*math.pi)/180
    return degres2radians
cosin45 =  math.cos(degres2radians(45) )
print('Cosinus 45 degrees = ', cosin45)
cosin40 = math.cos(degres2radians(40))
print('Cosinus 40 degrees = ', cosin40)
cosin60 = math.cos(degres2radians(60))
print('Cosinus 60 degrees = ', cosin60)

number = int(input("Enter 3 numbers "))
def separeting_numbers(number):
    first_num = number // 100
    second_num = number//10
    second_num = second_num %10
    third_num = number %10
    sum = first_num + second_num+third_num
    return sum
sum_numbers = separeting_numbers(number)
print('sum of your munber = '+ str(sum_numbers) )


catet_a = int(input("Enter catet "))
catet_b = int(input("Enter catet "))
def triangle_area_perimatr(catet_a,catet_b):
    c = math.sqrt(catet_a**2+catet_b**2)
    perimeter = (catet_a + catet_b + c)*2
    area = catet_a*catet_b*c
    return perimeter,area
perimetr , area = triangle_area_perimatr(catet_a,catet_b)
print("Perimetr = ", perimetr)
print('Area = ', area)











