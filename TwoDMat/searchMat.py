def searchMatrix(arr, x):
       row = len(arr)
       colm = len(arr[0])
       li=[]
       for i in range(row):
              for j in range(colm):
                     if(i == j):
                            c=1
                            break

       if(c ==1):
              print("found")

       else:
              print("not found")


arr=[[0, 6, 8, 9, 11],
       [20, 22, 28, 29, 31],
       [36, 38, 50, 61, 63],
       [64, 66, 100, 122, 128]]

searchMatrix(arr,212)