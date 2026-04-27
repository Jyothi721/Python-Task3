def greet(name):
    return f"Hello, {name}!"

# Function with *args
def add_numbers(*args):
    return sum(args)

# Function with **kwargs
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Lambda function
square = lambda x: x ** 2

# Testing
print(greet("Jyothi"))
print("Sum:", add_numbers(10, 20, 30, 40))

display_info(Name="Jyothi", Age=20, Course="Python")

print("Square of 5:", square(5))
