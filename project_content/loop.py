# Program demonstrating while loop, for loop, nested loop,
# pattern generation, and loop control statements

print("While Loop Example")

i = 1
while i <= 5:
    print("Number:", i)
    i += 1   # increase value of i

print("\nFor Loop Example")

for j in range(1, 6):
    print("Value:", j)
print("\nPattern Generation")

rows = 5

for i in range(rows):
    for j in range(i + 1):
        print("*", end=" ")
    print()   # move to next line

print("\nLoop Control Example")

for num in range(1, 10):

    if num == 3:
        continue   # skip number 3

    if num == 8:
        break      # stop loop at 8

    print(num)