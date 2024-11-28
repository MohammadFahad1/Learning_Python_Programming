# Default parameters
def sum(num1, num2, num3 = 0):
    result = num1 + num2 + num3
    return result

total = sum(99, 11)

# print("Sum:", total)


# Args
def all_sum(num1, num2,*numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum

total = all_sum(45, 30, 89, 11, 35, 56, 38, 77, 86)
print("All sum:", total)