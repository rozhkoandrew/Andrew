import store
import item
import electronics
import food
import clothes
class SaleInvoise():
    _lst_of_invoise = []
    _date = 0.0
    __record = []
    __record.append(clothes.Clothes.sell_dct)
    __record.append(electronics.Electronics.sell_dct)
    __record.append(food.Food.sell_dct)
    for x in __record:
        _lst_of_invoise.append(x)
    def __init__(self,date):
        self.date = date
        SaleInvoise.date = float(self.date)


    def remove_item(self):
        idx = 0
        for item_1 in SaleInvoise.__record:
            if item_1['item'] == self:
                del SaleInvoise.__record[idx]
            else:
                idx +=1

    def print_info(self):
        print('---------',float(self.date),'-------------')
        for item in SaleInvoise.__record:
            for key,value in item.items():
                print(key,' : ',value)
            print('----------------------')











