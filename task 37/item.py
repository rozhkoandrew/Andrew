class Item:
    __FORMAT_ATTR = "%-10s"
    __FORMAT_DELIM = ":"
    __FORMAT_VALUE = "%20s"
    __FORMAT_ALL = __FORMAT_ATTR + __FORMAT_VALUE


    def __init__(self,id,name,description,purchase_price,sell_price):
        self.id = id
        self.name = name
        self.description = description
        self.purchase_price = purchase_price
        self.sell_price = sell_price



    def format_row(self, attr_name, attr_value):
        attr_name_delim = attr_name + Item.__FORMAT_DELIM
        return Item.__FORMAT_ALL %(attr_name_delim,attr_value)

    def print_info(self):
        print()
        print("-----------------------------")
        print(self.format_row("ID", self.id))
        print(self.format_row("Name", self.name))
        print(self.format_row("Email", self.description))
        print(self.format_row("Phone", self.purchase_price))
        print(self.format_row("Phone", self.sell_price))