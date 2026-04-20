matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Summing All Elements

for row in range(len(matrix)):
    total = 0
    for column in range(len(matrix)):
        total += matrix[row][column]
    print("Sum for row", row, "is", total)


for column in range(len(matrix)):
    total = 0
    for row in range(len(matrix)):
        total += matrix[row][column]
    print("Sum for column", column, "is", total)