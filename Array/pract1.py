def leader(arr1):
    n = len(arr1)
    leaderElement = arr1[n-1]
    print(leaderElement,end=" ")
    for i in range(n-2,-1,-1):
        if(arr1[i]>leaderElement):
            print((arr1[i]),end=" ")
            leaderElement =arr1[i]
    # print(arr1)


arr =[16, 17, 4, 3, 5, 2]
leader(arr)