class Phone:
    manufactured = 'China'

    def __init__(self, owner, brand, price):
        self.owner = owner
        self.brand = brand
        self.price = price

    def send_sms(self, phone, sms):
        text = f'Sending to {phone} {sms}'
        print(text)

my_phone = Phone("Fahad", "Xiaomi", 17500)
print(my_phone.owner, my_phone.brand, my_phone.price)
my_phone.send_sms("017******19", "Hello world!")

her_phone = Phone("She", "iPhone", 150000)
print(her_phone.owner, her_phone.brand, her_phone.price)
her_phone.send_sms("015******80", "Gelo world!")