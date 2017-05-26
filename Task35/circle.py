import point
import math
class Circle:
    def __init__(self, x, y, radius):
        self.radius = radius
        self.x = x
        self.y = y

    def is_inside(self,point):
        distance = abs(math.sqrt((self.x-point.x)**2)+((self.y-point.y)**2))
        if distance <= self.radius:
            return True
        else:
            return False

