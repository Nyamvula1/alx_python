def square_matrix_simple(matrix=[]):
    square_matrix = []
    
    for row in matrix:
        square_row = []
        
        for i in row:
            square_row.append(i ** 2)
        
        square_matrix.append(square_row)
    return square_matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
if __name__ == '__main__':  
    new_matrix = square_matrix_simple(matrix)
    for row in new_matrix:
        print("[{}]".format(", ".join(map(str, row))))




