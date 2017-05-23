class Vehicle:
    def __init__(self,model,lenght,widght,speed):
        self.model = model
        self.lenght = lenght
        self.widght = widght
        self.speed = speed

    def print_info(self):
        print('-------------',self.__class__,'------------------')
        print('-------------', self.model ,'------------------')
        print('Lenght:  %d'%(self.lenght))
        print('Widght:  %d' % (self.widght))
        print('Speed:  %d' % (self.speed))



