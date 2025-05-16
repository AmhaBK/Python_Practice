m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of columns: "))

minefield = []
for i in range(m):
    row = []
    for j in range(n):
        element = int(input(f"Element at position ({i}, {j}): "))
        row.append(element)
    minefield.append(row)

neighboring_mines = [[0] * n for _ in range(m)]

for i in range(m):
    for j in range(n):
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                new_i = i + dx
                new_j = j + dy
                if 0 <= new_i < m and 0 <= new_j < n:
                    neighboring_mines[i][j] += minefield[new_i][new_j]

print("Neighboring Mines:")
for row in neighboring_mines:
    print(row)
