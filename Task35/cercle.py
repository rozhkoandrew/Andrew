import point
class Cercle(point.Point):
    def __init__(self,radius,cordinate):
        point.Point.__init__(self,cordinate)
        self.radius = radius

    def is_inside(self,corditate_1,cordinate_2,radius):
        if abs(corditate_1 - cordinate_2)<= radius:
            return True
        else:
            return False

