# global variable
balance = 3000
def buy_things(item, price):
    global balance
    print("Previous balance is: ", balance)
    balance -= price
    print(f'Balance after buying {item}', balance)

buy_things("Sunglass", 1000)
