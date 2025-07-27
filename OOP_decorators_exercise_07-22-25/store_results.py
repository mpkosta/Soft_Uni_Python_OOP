class store_results:
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        with open("results.txt", "a+") as file:
            result = self.function(*args, **kwargs)
            file.write(f"Function {self.function.__name__} was called. Result: {result}\n")
        return result

class store_results_with_parameters:
    def __init__(self, file_parameter):
        self.file_parameter = file_parameter

    def __call__(self, function):
        def wrapper(*args, **kwargs):
            with open(self.file_parameter) as file:
                result = function(*args, **kwargs)
                file.write(f"Function {self.function.__name__} was called. Result: {result}\n")
        return wrapper

@store_results
def add(a, b):
    return a + b

@store_results_with_parameters("results.txt")
def mult(a, b):
    return a * b

add(2, 2)
mult(6, 4)