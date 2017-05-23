import point
import math
class Cercle(point.Point):
    def __init__(self,x,y,radius):
        point.Point.__init__(self,x,y)
        self.radius = radius

    def is_inside(self,x1,y1,x2,y2,radius):
        distance = abs(math.sqrt((x1-x2)**2)+((y1-y2)**2))
        if distance <= radius:
            return True
        else:
            return False

