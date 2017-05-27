import item
import food
import electronics
import clothes
class Store:
    __dict = {}
    def __init__(self,electronics,food,clothes):
        self.electronics = electronics
        self.food = food
        self.clothes = clothes
        Store.__dict['electronics'] = self.electronics
        Store.__dict['food'] = self.food
        Store.__dict['clothes'] = self.clothes

    def print_balance(self):
        print('------------------------------------------------------')
        food_balance = Store.__dict['food'] - food.Food.food_bought_items
        electronics_balance = Store.__dict['electronics'] - electronics.Electronics.electronics_bought_items
        clothes_balance = Store.__dict['clothes'] - clothes.Clothes.clothes_bought_items
        if self == 'food':
            print(item.Item.format_row(Store.__dict, self +' balance' , food_balance))
        if self == 'clothes':
            print(item.Item.format_row(Store.__dict, self + ' balance', clothes_balance))
        if self == 'electronics':
            print(item.Item.format_row(Store.__dict, self + ' balance', electronics_balance))

    def add_item(self,item,qty):
        Store.__dict[item] += qty


    def remove_item(self,item,qty):
        Store.__dict[item] -= qty






