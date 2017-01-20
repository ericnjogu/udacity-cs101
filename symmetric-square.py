# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.
def symmetric(matrix):
    rows = [[] for i in range(len(matrix))]
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
    count = 0
    for l in rows:
        if l != cols[count]:
            return False
        count += 1
    return True

print symmetric([[]])
print symmetric([])
#print symmetric([[1, 2, 3],
#                [2, 3, 4],
#                [3, 4, 1]])
#>>> True

#print symmetric([["cat", "dog", "fish"],
#                ["dog", "dog", "fish"],
#                ["fish", "fish", "cat"]])
#>>> True

#print symmetric([["cat", "dog", "fish"],
#                ["dog", "dog", "dog"],
#                ["fish","fish","cat"]])
#>>> False

#print symmetric([[1, 2],
#                [2, 1]])
#>>> True

#print symmetric([[1, 2, 3, 4],
#                [2, 3, 4, 5],
#                [3, 4, 5, 6]])
#>>> False

#print symmetric([[1,2,3],
#                 [2,3,1]])
#>>> False
