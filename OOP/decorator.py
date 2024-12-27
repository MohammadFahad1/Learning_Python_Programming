import math 
import time

def timer(func):
    def inner(*args, **kargs):
        print("Time started")
        start = time.time()
        func(*args, **kargs)
        print("Time ended")
        end = time.time()
        print(f'Total time taken: {end-start}')
    return inner

# timer()()

@timer
def get_factorial(n):
    print("Factorial Starting")
    result = math.factorial(n)
    print(f'Factorial of {n} is: {result}')

get_factorial(10)

# Vejailla way to decorate
# timer(get_factorial)()
