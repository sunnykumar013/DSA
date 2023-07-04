def printT(mat):
    row = len(mat)
    col = len(mat[0])
    for i in range(row):
        for j in range(col):
            print(mat[i][j],end=" ")
        print(" ")


arr =[ [ 1, 2, 3, 4 ], [ 5, 6, 7, 8 ], [ 9, 10, 11, 12] ]
print(printT(arr))