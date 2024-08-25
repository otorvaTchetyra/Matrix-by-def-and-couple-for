def get_matrix(n, m, value):
    matrix = []
    for _ in range(n):
        row = []
        for _ in range(m):
            row.append(value)
        matrix.append(row)
    return matrix

matrix = get_matrix(3, 2, 1)
matrix1 = get_matrix(2,3,2)
matrix2 = get_matrix(1,4,3)
print(matrix) 
print(matrix1)
print(matrix2)