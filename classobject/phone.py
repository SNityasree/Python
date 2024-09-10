class phone: 
    def __init__(self,brand,price,chargetype):
        self.brand=brand
        self.price=price
        self.chargetype=chargetype
    def display(self):
        print("Brand:",self.brand)
        print("Price:",self.price)
        print("Chargetype:",self.chargetype)
       
samsung=phone("samsung",10000,"B-type")
samsung.display()
