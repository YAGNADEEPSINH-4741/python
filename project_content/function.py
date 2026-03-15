# Defining a function
def add(a, b):
    return a + b

# Calling the function
result = add(5, 3)
print("Sum:", result)

# Function with default parameter
def greet(name="User"):
    print("Hello", name)

greet("Yagna")
greet()

# Function returning multiple values
def calculate(a, b):
    return a+b, a*b

s, m = calculate(4, 2)
print("Sum:", s)
print("Product:", m)

# Lambda function
square = lambda x: x*x
print("Square:", square(5))

# Lambda with map
nums = [1,2,3,4]
squares = list(map(lambda x: x*x, nums))
print("Squares:", squares)