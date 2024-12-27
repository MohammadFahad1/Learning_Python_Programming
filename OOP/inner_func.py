# Function is a first class object
def double_decker():
    print("Starting the double decker")
    
    def inner_fun():
        print("Inside the inner")
        return 3000
    
    return inner_fun

# print(double_decker()())

def do_something(work):
    print("Work started")
    print(work())
    print("Work ended")

# do_something('Ami busy')

def coding():
    print("Coding in python")


# do_something(coding)

def sleeping():
    print("Sleeping")

do_something(sleeping)