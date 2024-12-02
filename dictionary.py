# Key value pair
# Dictionary
# Object
# Hash table
# Overlap with set
# {key: value, key: value, key: value}
person = {'name': "Kala Pakhi", 'address':  "Kaliapur", 'age': 23, 'job': "facebooker"}
print(person['name'])
print(person.keys())
print(person.values())
person['language'] = "Python"
person['name'] = "Shada Pakhi"
del person['age'] # Delete age property
print(person)

""" for item in person:
    print(item.upper()) """

# Looping through a dictionary
for key, value in person.items():
    print(key.capitalize(), ":", value)

numbers = [12,56,98,78,56,12,6,98]
for i, num in enumerate(numbers):
    print(i, num)