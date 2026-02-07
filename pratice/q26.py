n = int(input("Enter number of rows: "))

# Upper part
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Lower part
for i in range(2, n + 1):
    for j in range(i, n + 1):
        print(j, end=" ")
    print()
