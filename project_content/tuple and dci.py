# Creating a tuple
t = (10, 20, 30)

print("Tuple:", t)

# Tuple indexing and slicing
print("First element:", t[0])
print("Slice:", t[1:3])

# Tuple unpacking
a, b, c = t
print("Unpacked values:", a, b, c)

# Tuple operations
print("Length:", len(t))
print("Repetition:", t * 2)

# Creating a dictionary
student = {"name": "Yagna", "age": 20, "marks": 85}

print("Dictionary:", student)

# Accessing values
print("Name:", student["name"])

# Using get() method
print("Age:", student.get("age"))

# Adding new element
student["city"] = "Ahmedabad"

# Dictionary methods
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())