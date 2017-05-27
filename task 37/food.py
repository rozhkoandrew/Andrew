import item
class Food(item.Item):
    food_bought_items = 0
    sell_price = 0
    sell_dct = {}
    def __init__(self,id,name,description,purchase_price,sell_price,expire_date):
        Food.food_bought_items += 1
        super().__init__(id,name,description,purchase_price,sell_price)
        self.expire_date = expire_date
        Food.sell_price = self.sell_price
        Food.sell_dct['item'] = 'Food'
        Food.sell_dct['qty'] = Food.food_bought_items
        Food.sell_dct['sell price'] = Food.sell_price
        Food.sell_dct['summ'] = Food.sell_price * Food.food_bought_items

    def print_info(self):
        item.Item.print_info(self)
        print(self.format_row('Expire date', self.expire_date))
