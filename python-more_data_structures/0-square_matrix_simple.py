def square_matrix_simple(matrix=[]):
    square_matrix = []
    
    for row in matrix:
        square_row = []
        
        for i in row:
            square_row.append(i ** 2)
        
        square_matrix.append(square_row)
    return square_matrix

square_matrix_simple()
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
new_matrix = square_matrix_simple(matrix)
print(new_matrix)




