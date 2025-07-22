def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Start decorator function")
        func(*args, **kwargs)
        print("End decorator function")
    return wrapper


@my_decorator
def my_func():
    print("This is a test function.")


my_func()


def my_decorator_with_params(param1, param2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Decorator arguments: {param1}, {param2}")
            func(*args, **kwargs)

        return wrapper

    return decorator

@my_decorator_with_params("arg1", "arg2")
def my_func_with_params():
    print("This is a test function with params.")

my_func_with_params()