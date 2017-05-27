import sale_invoise
class SaleInvoiseJournal():
    def __init__(self):
        self.invoises = {}
        self.invoises[sale_invoise.SaleInvoise._date] = sale_invoise.SaleInvoise._lst_of_invoise

    def get_invoices(self,date):
        for key,value in self.invoises.items():
            if key == date:
                print(key)

