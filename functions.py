def func(string):
    rev_string = string[::-1]
    return rev_string

x=func("Tom")
print(x)

def square_matrix(matrix):
    for row in matrix:
        square_row = []
        for element in row:
            square_row.append(element ** 2)
        
    return square_row

result = square_matrix(matrix)
for row in result:
    print("[{}],".format(result))