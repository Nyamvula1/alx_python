def square_matrix(matrix=[]):
    result=[]
    for i in matrix:
        square_list = []
        for element in i:
            square_list.append(element ** 2)
        result.append(square_list)
    return result



