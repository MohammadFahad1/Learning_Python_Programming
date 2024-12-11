class Shopping:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, item, price, quantity):
        product = {'item': item, 'price': price, 'quantity': quantity}
        self.cart.append(product)

    def checkout(self, amount):
        total = 0
        for item in self.cart:
            total += item['price'] * item['quantity']
        if amount < total:
            print(f'Please provide {total - amount} more!')
        else:
            print(f'Here is your items and extra money {amount - total}.')


swapan = Shopping("Alan Swapan")
swapan.add_to_cart('Alu', 50, 6)
swapan.add_to_cart('Dim', 12, 24)
swapan.add_to_cart('Rice', 50, 5)

swapan.checkout(1000)

# print(swapan.cart)