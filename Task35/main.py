import point
import cercle




if __name__ =="__main__":
    point = point.Point(0)
    cercle = cercle.Cercle(4,10)
    print(cercle.is_inside( point.cordinate, cercle.cordinate,cercle.radius))





