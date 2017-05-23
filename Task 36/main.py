import vehicle
import train
import airplane

if __name__=='__main__':
    train_1 = train.Train('V-342',80,8,60,15)
    train_1.print_info()
    train_1.add_carriage_or_reduce(-2)
    train_1.print_info()
    airplane_1 = airplane.Airplane('Boing-747',40,12,200,300)
    airplane_1.print_info()
