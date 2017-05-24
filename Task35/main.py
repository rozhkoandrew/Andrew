import point
import cercle




if __name__ =="__main__":
    point_1 = point.Point(0,0)
    cercle_piont = point.Point(10,10)
    cercle = cercle.Cercle(cercle_piont,4)
    print(cercle.is_inside( point_1.x,point_1.y,cercle_piont.x,cercle_piont.y ,cercle.radius))





