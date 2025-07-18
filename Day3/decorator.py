import inspect


def decorator(func):
    def wrapper():
        print("Before calling the function.")
        func()
        print("after calling the function")
    return wrapper

#applying the decorator to a funcytion

@decorator
def greet():
    print("hello world**")
greet()

print(inspect.signature(decorator))