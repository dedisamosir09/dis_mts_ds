def matrix_script(matrix):
    rows, cols = map(int, matrix[0].split())  
    result = []

    for col in range(cols):
        col = ''.join(matrix[row][col] if col < len(matrix[row]) else ' ' for row in range(1, rows + 1))
        result.append(' '.join(filter(str.isalnum, col)))

    return '\n'.join(result)

list_matrix = ["7 3","My ","Sa!","T-!","$j ","#a-","jy_","aa-"]

result = matrix_script(list_matrix)
print(result)
