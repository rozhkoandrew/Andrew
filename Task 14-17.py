import math
def is_even_number(number):
    cheking = number%2
    return cheking==0
print(is_even_number(2))

#first_point = [2,7]
radius_of_first_cercle = 27
#second_point = [5,8]
radius_of_second_cercle = 25
#coordinates = [first_point,second_point]"""
coordinates = [1,2,1,2]
#def identify_crossing(x1,y1,x2,y2):
def circles_crossing(radius_of_first_cercle,radius_of_second_cercle,*coordinates):
    distance = math.sqrt((coordinates[0]-coordinates[1])**2)+((coordinates[2]-coordinates[3])**2)
    #distance = math.sqrt((x1-y1)**2) +((x2-y2)**2)
    #return distance
    radius_sum = radius_of_first_cercle + radius_of_second_cercle
    delta = distance - radius_sum
    radius_diferrense = radius_of_first_cercle - radius_of_second_cercle
    #return is_crossing
    if delta >=0:
        return False
    #elif abs(radius_diferrense) > 0 and distance < abs(radius_of_second_cercle - radius_of_first_cercle):
    elif  0< abs(radius_diferrense) > distance:
        return False
    else:
        return True
print(circles_crossing(radius_of_first_cercle,radius_of_second_cercle,*coordinates))

"""first_train_speed = 24
turn_will_be = (60/ first_train_speed) * 4
second_train_speed = 30
collision_will_be = (60/second_train_speed)*6
print(turn_will_be)
print(collision_will_be)"""

def identify_collision(first_train_speed,second_train_speed):
    turn_will_be = (60 / first_train_speed) * 4
    collision_will_be = (60 / second_train_speed) * 6
    if turn_will_be <= collision_will_be:
        return True
    else:
        return False
print(identify_collision(22,25))

def quadratic_equation(a,b,c):
    discr = b**2-4*a*c
    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        return x1,x2
    elif discr == 0:
        x3 = -b / (2 * a)
        return x3, None
    else:
        return None, None
quadratic_equation = quadratic_equation(10,31,13)
print(quadratic_equation)



















