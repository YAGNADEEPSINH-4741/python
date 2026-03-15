# Taking input from the user
name = input("Enter your name: ")     # user enters name
age = input("Enter your age: ")       # user enters age

# Converting age into integer
age = int(age)

# Calculating birth year (example calculation)
birth_year = 2026 - age

# Displaying output
print("\n----- User Information -----")

print("Name:", name)                  # print name
print("Age:", age)                    # print age
print("Estimated Birth Year:", birth_year)  # print calculated birth year