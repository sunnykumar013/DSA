def principalMAtrix(arr):

    row = len(arr)
    colm = len(arr[0])
    diamat=[]
    for i in range(row):
        for j in range(colm):
            if(i==j):
                diamat.append(arr[i][j])

    return diamat


arr=[ [ 1, 2, 3, 4 ],
                    [ 5, 6, 7, 8 ],
                    [ 1, 2, 3, 4 ],
                    [ 5, 6, 7, 8 ] ]

print(principalMAtrix(arr))