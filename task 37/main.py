import item
import electronics
import clothes
import food
import store
import sale_invoise
import sale_invoise_journal
if __name__ == '__main__':

    elec = electronics.Electronics(505,'Iphone','Cellphone',300,800,'A')
    elec2 = electronics.Electronics(504,'Iphone','Cellphone',300,800,'A')
    elec3 = electronics.Electronics(504,'Iphone','Cellphone',300,800,'A')
    clothes_1 =clothes.Clothes(202,'T-shirt,','Wear',4,20,'M')
    clothes.Clothes(202, 'T-shirt,', 'Wear', 4, 20, 'M')
    clothes.Clothes(202,'T-shirt,','Wear',4,20,'M')
    clothes.Clothes(202,'T-shirt,','Wear',4,20,'M')
    clothes.Clothes(202, 'T-shirt,', 'Wear', 4, 20, 'M')
    elec.print_info()
    clothes_1.print_info()
    store_1 = store.Store(300,400,500)
    store.Store.print_balance('food')
    store.Store.print_balance('electronics')
    store.Store.print_balance('clothes')
    store.Store.add_item(store_1,'clothes',1000)
    store.Store.remove_item(store_1,'electronics',100)

    day1 = sale_invoise.SaleInvoise(19.01)
    sale_invoise.SaleInvoise.print_info(day1)
    elec = electronics.Electronics(505,'Iphone','Cellphone',300,800,'A')
    elec2 = electronics.Electronics(504,'Iphone','Cellphone',300,800,'A')
    elec3 = electronics.Electronics(504,'Iphone','Cellphone',300,800,'A')
    food = food.Food(303,'Apple,','Fruit',1,5,20.03)
    clothes_1 =clothes.Clothes(202,'T-shirt,','Wear',4,20,'M')
    clothes.Clothes(202,'T-shirt,','Wear',4,20,'M')
    clothes.Clothes(202,'T-shirt,','Wear',4,20,'M')
    elec.print_info()
    food.print_info()
    clothes_1.print_info()
    store.Store.print_balance('food')
    store.Store.print_balance('electronics')
    store.Store.print_balance('clothes')
    store.Store.add_item(store_1,'clothes',500)
    store.Store.remove_item(store_1,'electronics',100)
    #sale_invoise.SaleInvoise.remove_item('Clothes')
    day2 = sale_invoise.SaleInvoise(20.01)
    sale_invoise_journal.SaleInvoiseJournal.get_invoices(19.01)
    a = sale_invoise_journal.SaleInvoiseJournal.get_invoices(day2)
