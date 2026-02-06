rows = 5

for i in range(1, rows + 1):
    if i % 2 == 1:   # odd row → start with capital A
        ch = ord('A')
    else:           # even row → start with small a
        ch = ord('a')

    for j in range(i):
        print(chr(ch + j), end=" ")
    print()