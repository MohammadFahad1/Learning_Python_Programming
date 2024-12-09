class Shop:
    shopping_mall = "Jamuna" #Class Attribute
    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = [] #Instance Attribute

    def add_to_cart(self, item):
        self.cart.append(item)

mehzabeen = Shop("Mehzabeen")
mehzabeen.add_to_cart("Phone")
mehzabeen.add_to_cart("Shoe")
print(mehzabeen.cart)

nisho = Shop("Nisho")
nisho.add_to_cart("Watch")
nisho.add_to_cart("Hat")
print(nisho.cart)

apurbo = Shop("Apurbo")
apurbo.add_to_cart("Chironi")
apurbo.add_to_cart("Bike")
apurbo.add_to_cart("Iphone")
print(apurbo.cart)