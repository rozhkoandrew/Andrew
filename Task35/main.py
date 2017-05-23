import point
import cercle




if __name__ =="__main__":
    point = point.Point(0,0)
    cercle = cercle.Cercle(10,10,4)
    print(cercle.is_inside( point.x,point.y,cercle.x,cercle.y ,cercle.radius))





