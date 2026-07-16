def rotate(matrix):
    n = len(matrix)
    m = len(matrix[0])
    result = [[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]
    for i in range(n):
        for j in range(m):
            result[j][(n-1)-i] = matrix[i][j]
    return result


# OPTIMAL 
def rotate(matrix):
    for i in range(len(matrix)):
        for j in range(i+1, len(matrix[0])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(len(matrix)):
        matrix[i].reverse()
