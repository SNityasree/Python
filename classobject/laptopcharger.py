class laptop():
    charge="C Type"
    def __init__(self):
        self.brand=""
        self.price=34
    def setprice(self,price):
        self.price=price
    def getprice(self):
        print(self.price)
    @classmethod
    def changecharge(cls):
        cls.charge="B Type"
        print("Charger type changed into B")
    @staticmethod
    def info():
        print("This is laptop class")
        

hp=laptop()
hp.setprice(2000)

hp.getprice()
laptop.changecharge()
hp.info()




        
      
