numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

remaining = []

for num in numbers:
    if num % 2 != 0:  
        remaining.append(num)

print("List after removing even numbers:", remaining)
