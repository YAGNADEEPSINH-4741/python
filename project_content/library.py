import math
import random

# Global variable
x = 10

# Function demonstrating local and global scope
def scope_demo():
    global x
    x = x + 5
    y = 20  # local variable
    print("Inside function:")
    print("x =", x)
    print("y =", y)

scope_demo()

print("Outside function x =", x)

# Using math module
print("Square root:", math.sqrt(16))
print("Value of pi:", math.pi)

# Using random module
print("Random number:", random.randint(1,10))

numbers = [1,2,3,4,5]
random.shuffle(numbers)
print("Shuffled list:", numbers)