import item
class Clothes(item.Item):
    clothes_bought_items = 0
    sell_price = 0
    sell_dct = {}
    def __init__(self,id,name,description,purchase_price,sell_price,size):
        Clothes.clothes_bought_items += 1
        super().__init__(id,name,description,purchase_price,sell_price)
        self.size = size
        Clothes.sell_price = self.sell_price
        Clothes.sell_dct['item'] = 'Clothes'
        Clothes.sell_dct['qty'] = Clothes.clothes_bought_items
        Clothes.sell_dct['sell price'] = Clothes.sell_price
        Clothes.sell_dct['summ'] = Clothes.sell_price * Clothes.clothes_bought_items

    def print_info(self):
        item.Item.print_info(self)
        print(self.format_row('size', self.size))

