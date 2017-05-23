class Godzila:
    def __init__(self,stomach_capacity,stomach_fullness=0):
        self.stomach_capacity = stomach_capacity
        self.stomach_fullness = stomach_fullness
        self.stomach_limit = (self.stomach_capacity//100)* 90


    def is_godzila_full(self,man):
        if self.stomach_fullness + man.weight  >= self.stomach_limit:
            return False
        else:
            return True


    def people_eating(self, people ):
        self.stomach_fullness += people.weight
        print('Now it is %d - kg inside , godzila can eat  %d - kg more ' %
              (self.stomach_fullness, self.stomach_limit - self.stomach_fullness))















''' def people_eating(self,lst_poeple,):
        for man in lst_poeple:
            if self.stomach_fullness + man.weight >= self.stomach_limit:
            #if self.stomach_fullness >= self.stomach_limit:
                print('Stomach is full %d kg inside ' % (self.stomach_fullness))
                break

            else:
                self.stomach_fullness += man.weight
                print('Now it is %d - kg inside , godzila can eat  %d - kg more ' %
                      (self.stomach_fullness, self.stomach_limit - self.stomach_fullness ))'''






















'''    def people_eating(self,people_lst):
        for man in people_lst:
            self.stomach_fullness += 1
            if (self.stomach_fullness * 100)//self.stomach_capacity == 90:
                print(' Godzila is full,and cannot eat people ,%d people inside, and %d remain '%(
                    self.stomach_fullness,self.stomach_fullness - len(people_lst)))'''



