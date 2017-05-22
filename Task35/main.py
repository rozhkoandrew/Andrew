import point
import cercle




if __name__ =="__main__":
    point = point.Point(20,5)
    cercle = cercle.Cercle(20,20,4)
    print(cercle.is_inside( point.coordinates, cercle.center_cordinate,cercle.radius))



