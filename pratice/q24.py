n = int(input("Enter Number :")) 
num = 1
rows = []

# Upper half
for i in range(1, n + 1):
    row = []
    for _ in range(i):
        row.append(num)
        num += 1
    rows.append(row)

# Print upper half
for r in rows:
    print(*r)

# Print lower half (reverse)
for r in reversed(rows[:-1]):
    print(*r[::-1])
