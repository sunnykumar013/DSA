def naturalNu(arr1,n):
    sum1 = ((n+1) * (n+2))//2
    sum2=0
    for i in range(len(arr1)):
        sum2 +=arr1[i]

    miss = sum1-sum2
    print(miss)

arr=[1, 2, 4, 6, 3, 7, 8]
naturalNu(arr,len(arr))


