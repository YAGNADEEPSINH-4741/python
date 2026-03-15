# Creating a list
numbers = [1, 2, 3, 4, 5]

print("List:", numbers)

# Basic operations
print("Length:", len(numbers))
print("Concatenation:", numbers + [6, 7])
print("Repetition:", numbers * 2)

# Membership testing
print("3 in list:", 3 in numbers)

# Indexing and slicing
print("First element:", numbers[0])
print("Last element:", numbers[-1])
print("Slice:", numbers[1:4])

# List is mutable
numbers[0] = 10
print("Modified list:", numbers)

# List methods
numbers.append(6)
numbers.insert(2, 20)
numbers.remove(4)
print("After methods:", numbers)

# Sorting and reversing
numbers.sort()
numbers.reverse()
print("Sorted and reversed:", numbers)

# List comprehension
squares = [x*x for x in range(1,6)]
print("Squares:", squares)

# Nested list (matrix)
matrix = [[1,2,3],[4,5,6],[7,8,9]]

print("Matrix element [1][2]:", matrix[1][2])

# Iterating nested list
for row in matrix:
    for item in row:
        print(item, end=" ")
    print()