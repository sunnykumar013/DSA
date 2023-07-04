def nine(mat):
    row = len(mat)
    colm = len(mat[0])
    print(row, colm)
    for i in range(row):
        for j in range(i+1,colm):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

    for i in range(row):
        j=0
        k = row-1
        while(j<=k):
            mat[i][j],mat[i][k] = mat[i][k], mat[i][j]
            j +=1
            k -=1


    for i in range(row):
        for j in range(colm):
            print(mat[i][j],end=" ")

        print()

    # print(mat)


A =  [[1,2,3],[4,5,6],[7,8,9]]

print(nine(A))