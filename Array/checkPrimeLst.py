def checkP(arr):
    n = len(arr)
    res=[]

    for i in range(n):
        c = 0

        for j in range(2,arr[i]):
            if(arr[i]%j == 0):
               # print("ss", arr[i])
               c=1
               break

        if(c==0):
            # print(c,arr[i])
            res.append(arr[i])


    return res


arr =[11,22,13,56,1,2,568]
print(checkP(arr))