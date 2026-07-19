from functools import wraps

def my_decorator(func):  # func can be any name, but for to remember, we use function
    @wraps(func)

    def my_func():
        print("before func runs")
        func()
        print("after func runs")
    return my_func

@my_decorator
def add_code():
    print("hello from decorators")

add_code()
print(add_code.__name__)