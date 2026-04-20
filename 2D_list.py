sum = 0
matrix = [[1,2,3], 
          [4,5,6], 
          [7,8,9],]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i==j:
            sum += matrix[i][j]
print(sum)



for col in range(len(matrix)):
    for row in range(len(matrix[col])):
        print(matrix[row][col], end=" ")
    print()


