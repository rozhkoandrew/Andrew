import item
class Electronics(item.Item):
    electronics_bought_items = 0
    sell_price = 0
    sell_dct = {}
    def __init__(self,id,name,description,purchase_price,sell_price,energy_class):
        Electronics.electronics_bought_items += 1
        super().__init__(id,name,description,purchase_price,sell_price)
        self.energy_class = energy_class
        Electronics.sell_price = self.sell_price
        Electronics.sell_dct['item'] = 'Electronics'
        Electronics.sell_dct['qty'] = Electronics.electronics_bought_items
        Electronics.sell_dct['sell price'] = Electronics.sell_price
        Electronics.sell_dct['summ'] = Electronics.sell_price * Electronics.electronics_bought_items

    def print_info(self):
        item.Item.print_info(self)
        print(self.format_row('Energy class', self.energy_class))
