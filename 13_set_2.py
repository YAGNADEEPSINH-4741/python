# Define sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Set 1:", set1)
print("Set 2:", set2)

# Unique values (Union)
print("\nUnique values (Union):", set1 | set2)

# Common values (Intersection)
print("Common values (Intersection):", set1 & set2)

# Values only in Set 1 (Difference)
print("Values only in Set 1:", set1 - set2)

# ----------------------------------------

# Duplicate value list
numbers = [12, 18, 25, 31, 37, 42, 48, 53, 57, 61,
           70, 74, 78, 82, 86, 92, 96, 99, 12, 18, 48]

print("\nOriginal List:", numbers)
print("Length of List:", len(numbers))

# Convert list into set (removes duplicates)
unique_numbers = set(numbers)

print("Unique Numbers:", unique_numbers)
print("Length after Removing Duplicates:", len(unique_numbers))

# Find duplicates (extra useful improvement)
duplicates = {num for num in numbers if numbers.count(num) > 1}
print("Duplicate Numbers:", duplicates)
