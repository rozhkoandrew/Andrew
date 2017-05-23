import vehicle
class Airplane(vehicle.Vehicle):
    def __init__(self,model,lenght,widght,capacity,speed):
        vehicle.Vehicle.__init__(self,model, lenght, widght, speed)
        self.capacity = capacity
        self.bagage_capacity = capacity * 2

    def print_info(self):
        vehicle.Vehicle.print_info(self)
        print('Baggage amount:  %d' % (self.bagage_capacity))
        print('Capacity:  %d' % (self.capacity))


