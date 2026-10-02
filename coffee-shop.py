
class Drink:
    def __init__(self, name, size, price):
        self.name = name
        self.size = size
        self.price = price

class Customer:
    def __init__(self, name):
        self.name = name

    def order_drink(self, drink):
        print(f"{self.name} ordered {drink.name}")

    def pay(self, drink):
        print(f"{self.name} paid {drink.price}")

class Barista:
    def __init__(self, name):
        self.name = name

    def prepare_drink(self, drink):
        print(f"{self.name} prepared {drink.name}")
drink1 = Drink("Latte", "Medium", 1500)
c1 = Customer("Ahmed")
b1 = Barista("Ali")

c1.order_drink(drink1)
b1.prepare_drink(drink1)
c1.pay(drink1)
