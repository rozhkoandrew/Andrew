import math
def degres2radians(degres):
    radians = (degres*math.pi)/180
    cos = math.cos(radians)
    return radians,cos
print(degres2radians(45))
print(degres2radians(40))
print(degres2radians(60))

number = int(input("Enter 3 numbers "))
def separeting_numbers(number):
    first_num = number // 100
    second_num = number//10
    second_num = second_num %10
    third_num = number %10
    sum = first_num + second_num+third_num
    return sum
sum = separeting_numbers(number)
print('sum of your munber = '+ str(sum) )


a = int(input("Enter catet "))
b = int(input("Enter catet "))
def triangle(a,b):
    c = math.sqrt(a**2+b**2)
    perimeter = (a + b + c)*2
    area = a*b*c
    return perimeter,area
perimetr , area = triangle(a,b)
print("Perimetr = ", perimetr)
print('Area = ', area)











