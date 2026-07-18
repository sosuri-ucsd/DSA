def spiral_matrix(matrix):
    if not matrix or not matrix[0]:
        return []
    
    result = []

    top = 0
    left = 0
    bottom = len(matrix) - 1
    right = len(matrix[0]) - 1

    while top <= bottom and left <= right:
        
