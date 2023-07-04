def matTrans(arr):
    row = len(arr)
    colm = len(arr[0])
    matTran=[[0 for i in range(row)] for j in range(colm)]

    for i in range(row):
        for j in range(colm):
            matTran[i][j] = arr[j][i]

        # print(end=" ")
    for i in range(len(matTran)):
        for j in range(len(matTran[0])):
            print(matTran[i][j],end=" ")
        print()



arr = [[1, 1, 1, 1],
       [2, 22, 12, 2],
       [3, 3, 30, 3],
       [4, 43, 4, 4]]
matTrans(arr)


