# By Dimitris_GR from forums
# Modify Problem Set 31's (Optional) Symmetric Square to return True 
# if the given square is antisymmetric and False otherwise. 
# An nxn square is called antisymmetric if A[i][j]=-A[j][i] 
# for each i=0,1,...,n-1 and for each j=0,1,...,n-1.

def antisymmetric(matrix):
    size = len(matrix)
    rows = [[] for i in range(size)]
    if len(rows) > 0:
        cols = [[] for i in range(len(matrix[0]))]
    else:
        cols = []
    if len(rows) != len(cols):
        return False
    row_count = 0
    for row in matrix:
        col_count = 0
        for col in row:
            rows[row_count].append(col)
            cols[col_count].append(col)
            col_count += 1
        row_count += 1
        
    for i in range(size):
        for j in range(size):
            if rows[i][j] + cols[i][j] != 0:
                return False
    return True



# Test Cases:
print antisymmetric([[]])

print antisymmetric([])

print antisymmetric([[0, 1, 2], 
                     [-1, 0, 3], 
                     [-2, -3, 0]])   
#>>> True

print antisymmetric([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]])
#>>> True

print antisymmetric([[0, 1, 2], 
                     [-1, 0, -2], 
                     [2, 2,  3]])
#>>> False

print antisymmetric([[1, 2, 5],
                     [0, 1, -9],
                     [0, 0, 1]])
#>>> False

