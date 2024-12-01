def multiple():
    return 3, 4

# print(multiple()) # returns a tuple
things = 'Pen', 'Triped', 'Water bottle', 'charger', 'phone', 'web cam'
# print(things)
""" print(things[0])
print(things[0:3:2])
print(things[::-1]) """

if "phone" in things:
    print("Phone Exists")

# things[0] = "Wagon" # 'tuple' object does not support item assignment
# print(things[0])
# print(len(things))
mega = ([2,3,4], [5,6,7])
# print(type(mega))
print(mega[0][1])
mega[0][1] = 333
print(mega[0][1])

# By default tuples are immutable but immutables objects inside the tuple like a list item can be changed, the above example shows that