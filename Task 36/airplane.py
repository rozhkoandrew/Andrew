import vehicle
class Airplane(vehicle.Vehicle):
    def __init__(self,model,lenght,widght,capacity,speed,free_meal = False):
        super().__init__(model, lenght, widght, speed)
        self.capacity = capacity
        self.bagage_capacity = capacity * 2
        self.free_meal = free_meal



    def include_free_meal(self, free_meal):
        self.free_meal = free_meal


    def print_info(self):
        vehicle.Vehicle.print_info(self)
        print('Baggage amount:  %d' % (self.bagage_capacity))
        print('Capacity:  %d' % (self.capacity))
        if self.free_meal == True:
            print('In this voyage you have meal for free')
        elif self.free_meal == False:
            print('No free meal in this voyage')



