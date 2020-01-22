class Mobile:
    __discount = 50
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand

    def purchase(self):
        total = self.price - self.price * Mobile.__discount / 100
        print (self.brand, "mobile with price", self.price, "is available after discount at", total)

    @staticmethod
    def enable_discount():
        Mobile.set_discount(50)

    @staticmethod
    def disable_discount():
        Mobile.set_discount(0)

    @staticmethod
    def get_discount():
        return Mobile.__discount

    @staticmethod
    def set_discount(discount):
        Mobile.__discount = discount

mob1=Mobile(20000, "Apple")
mob2=Mobile(30000, "Apple")
mob3=Mobile(5000, "Samsung")

Mobile.disable_discount()

mob1.purchase()

Mobile.enable_discount()

mob2.purchase()

Mobile.disable_discount()

mob3.purchase()