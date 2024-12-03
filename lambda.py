# Lambda
""" 
def doubled(x):
    return x*2 """

doubled = lambda num: num * 2
squared = lambda num: num * num
result = doubled(44)
output = squared(9)

add = lambda x, y: x + y
sum = add(11, 33)
# print(sum)

# result = doubled(44)
# print(result)

numbers = [12,56,98,78,56,12,6,98]
# doubled_nums = map(doubled, numbers)
doubled_nums = map(lambda x: x * 2, numbers)
squared_nums = map(lambda x: x * x, numbers)
print(numbers)
print(list(doubled_nums))
print(list(squared_nums))

actors = [
    {'name': 'Sabana', 'age': 65},
    {'name': 'Sabnoor', 'age': 45},
    {'name': 'Sabila Noor', 'age': 30},
    {'name': 'Srabonti', 'age': 38},
    {'name': 'Shakib Khan', 'age': 47},
]

juniors = filter(lambda actor: actor['age'] < 40, actors)
fivers = filter(lambda actor: actor['age'] % 5 == 0, actors)
print(list(juniors))
print(list(fivers))