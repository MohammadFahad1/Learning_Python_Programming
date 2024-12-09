def call():
    print('calling someone i dont know')
    return 'call done'

class Phone:
    price = 17500
    color = 'blue'
    brand = 'Xiaomi'
    feature = ['camera', 'speaker', 'hammer']

    def call(self):
        print('calling one person')

    def send_sms(self, phone, sms):
        text = f'Sending SMS to 0{phone} and message: {sms}'
        return text

my_phone = Phone()
# print(my_phone.feature)
# my_phone.call()
result = my_phone.send_sms(179306019, 'How are you ?')
print(result)