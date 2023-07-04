def zigzags(arr):
    row =len(arr)
    colmn = len(arr[0])
    print(colmn,row)
    curr_row = curr_colm =0

    zig=[]
    moveUp =True
    while(len(zig) != row * colmn):
        # print((len(zig)),row * colmn)
        if(moveUp):

            while(curr_row >= 0 and curr_colm<colmn):
                # print(curr_colm, curr_row)
                zig.append(arr[curr_row][curr_colm])
                curr_colm += 1
                curr_row -= 1

            if(curr_colm == colmn ):
                curr_colm -= 1
                curr_row += 2

            else:
                curr_row += 1

            moveUp = False

        else:
            while(curr_colm>=0 and curr_row < row):
                zig.append(arr[curr_row][curr_colm])
                curr_colm -= 1
                curr_row +=1

            if (curr_row== row ):
                curr_colm += 2
                curr_row -= 1

            else:
                curr_colm += 1

            moveUp = True

    return zig






arr =[[1,2,3],[4,5,6],[7,8,9]]
 
print(zigzags(arr))