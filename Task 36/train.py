import vehicle
class Train(vehicle.Vehicle):
    def __init__(self,model,lenght,widght,speed,carriage_n,):
        super().__init__(model,lenght,widght,speed)
        self.carriage_n = carriage_n
        self.capacity = self.carriage_n * 30
        self.speed = self.speed - self.carriage_n

    def add_carriage_or_reduce(self, carriage_number):
        # add carrige to your traine
        self.carriage_n += carriage_number
        self.capacity = self.carriage_n * 30


    def print_info(self):
        vehicle.Vehicle.print_info(self)
        print('Carrige number:  %d'%(self.carriage_n))
        print('Capacity:  %d' % (self.capacity))


