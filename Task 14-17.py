import math
def is_even_number(number):
    cheking = number%2
    return cheking==0
print(is_even_number(2))

#first_point = [2,7]
radius_of_first_cercle = 4
#second_point = [5,8]
radius_of_second_cercle = 25
#coordinates = [first_point,second_point]"""
coordinates = [4,10,5,6]
#def identify_crossing(x1,y1,x2,y2):
def identify_crossing(radius_of_first_cercle,radius_of_second_cercle,*coordinates):
    distance = math.sqrt((coordinates[0]-coordinates[1])**2)+((coordinates[2]-coordinates[3])**2)
    #distance = math.sqrt((x1-y1)**2) +((x2-y2)**2)
    #return distance
    radius_sum = radius_of_first_cercle + radius_of_second_cercle
    is_crossing = distance - radius_sum
    #return is_crossing
    if is_crossing >=0:
        return True
    else:
        return False
print(identify_crossing(radius_of_first_cercle,radius_of_second_cercle,*coordinates))

"""first_train_speed = 24
turn_will_be = (60/ first_train_speed) * 4
second_train_speed = 30
collision_will_be = (60/second_train_speed)*6
print(turn_will_be)
print(collision_will_be)"""

def identify_collision(first_train_speed,second_train_speed):
    turn_will_be = (60 / first_train_speed) * 4
    collision_will_be = (60 / second_train_speed) * 6
    if turn_will_be < collision_will_be:
        return True
    else:
        return False
print(identify_collision(22,25))













