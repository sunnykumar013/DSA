"""def pyTrip(arr):
    n=len(arr)
    lst=[]

    for i in range(n):
        for j in range(i+1,n):

            for k in range(j+1,n):

                x =arr[k]*arr[k]
                y =arr[j]*arr[j]
                z=arr[i]*arr[i]
                if(x == y+z or y == x+z or z == x+y):
                    lst = lst + [arr[i],arr[j],arr[k]]
                    # print(arr[i],arr[j],arr[k])

    return lst



arr=[9, 2, 3, 4, 8, 5, 6, 10]
print(pyTrip(arr))
# pyTrip(arr)

    """
import math


def tripletArr(arr):
    n = len(arr)

    for i in range(n):
        arr[i] = arr[i] * arr[i]

    arr.sort()
    # print(arr)

    for i in range(n-1,1,-1):

        j=0
        k = i-1
        while(j<k):

            if (arr[j] + arr[k] == arr[i]):
                print(math.sqrt(arr[i]), math.sqrt(arr[j]), math.sqrt(arr[k]))
                break

            else:
                if(arr[j] + arr[k]< arr[i]):
                    j = j + 1

                else:
                    k = k - 1



arr=[9, 2, 3, 4, 8, 5, 6, 10]

tripletArr(arr)


