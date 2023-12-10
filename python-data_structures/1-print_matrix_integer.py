def square_matrix(matrix=[]):
    result=[]
    for row in matrix:
        square_row = []
        for element in row:
            square_row.append(element ** 2)
        result.append(square_row)
    return result

result = square_matrix(matrix=[])
for row in result:
    formatted_row = ', '.join(map("{}".format, row))
    print("[{}],".format(formatted_row))






