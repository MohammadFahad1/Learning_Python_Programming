class Shop:
    cart = [] # Class Attribute
    def __init__(self, buyer):
        self.buyer = buyer

    def add_to_cart(self, item):
        self.cart.append(item)

mehzabeen = Shop("Mehzabeen")
mehzabeen.add_to_cart("Shoes")
mehzabeen.add_to_cart("Phone")
print(mehzabeen.cart)

nisho = Shop("Nisho")
nisho.add_to_cart("Cap")
nisho.add_to_cart("Watch")
print(nisho.cart)