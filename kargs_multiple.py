def full_name(first, last):
    name = f'{first} {last}'
    return name

# Take parameters in order
""" name = full_name('Fahad', 'Munshi') """
""" name = full_name(last='Munshi', first='Fahad') """
# print(name)
""" def famous_name(first, last, title, addition):
    name = f'{title} {first} {last} {addition}'
    return name

name = famous_name(first="Fahad", last="Munshi", title="Md.", addition="Engr") """


""" def famous_name(first, last, title, **addition):
    name = f'{title} {first} {last}'
    # print(addition['height'])
    for key, value in addition.items():
        print(key, value)

name = famous_name("Fahad", "Munshi", "Md.", height="5.5 fit") """

""" def famous_name(first, last, *addition):
    name = f'{addition[1]} {first} {last}'
    return name

name = famous_name(last="Fahad", first="Munshi", title="Md.", title1="Mr.")
print(name) """

# return multiple things
def a_lot(num1, num2):
    sum = num1 + num2
    mult = num1 * num2
    remain = num1 - num2
    return sum, mult, remain

everyting = a_lot(10, 20)
print(everyting)