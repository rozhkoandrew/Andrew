import point
class Cercle(point.Point):
    def __init__(self,radius,x,y):
        point.Point.__init__(self,x,y)
        self.center_cordinate = (self.x - self.y) ** 2
        self.radius = radius

    def is_inside(self,corditate_1,cordinate_2,radius):
        if corditate_1 - cordinate_2 <= radius:
            return True
        else:
            return False

