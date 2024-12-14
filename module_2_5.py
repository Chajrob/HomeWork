def get_matrix (n, m, value):
    matrix = []
    for i in range(0,n):
        matrix.insert(0,[])
        for i in range(0,m):
            matrix[0].insert(i, value)
    print(matrix)
    return matrix
get_matrix(2, 3, 10)
