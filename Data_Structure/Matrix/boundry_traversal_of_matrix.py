matrix = [
    [1,2,3],
    [4,5,6,],
    [7,8,9]
]

def boundary_traversal(matrix):
    row = len(matrix)
    col = len(matrix[0]) if row > 0 else 0 
    for i in range (row):
        for j in range (col) :
            if i ==0 or j == 0 or i == row-1 or j == col -1:
                print(matrix[i][j],end=' ')

boundary_traversal(matrix)
