# Decorator is a function that takes another function as argument and returns a function
# It denoted with @ symbol above the function the are decorating

def decorator(fun):
    def wrapper():
        print("Transaction Initiated... ")
        fun()
        print("Transaction Completed Successfully....")
    return wrapper

@decorator
def hello():
    print(".... Executing all steps of Transaction Logic.....")

hello()

# hello1 = decorator(hello)
# hello1()