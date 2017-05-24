import point
import math
class Cercle:
    def __init__(self,point,radius):
        self.radius = radius
        self.point = point

    def is_inside(self,x1,y1,x2,y2,radius):
        distance = abs(math.sqrt((x1-x2)**2)+((y1-y2)**2))
        if distance <= radius:
            return True
        else:
            return False

