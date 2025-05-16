matrix = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

print("Enter values for the 3x3 matrix:")

for i in range(3):
    for j in range(3):
        value = int(input("({}, {}): ".format(i, j)))
        matrix[i][j] = value

sum_diagonal = 0

for i in range(3):
    sum_diagonal += matrix[i][i]

print("Matrix:")
for row in matrix:
    print(row)

print("Sum of main diagonal values:", sum_diagonal)
