def pairsum(arr1,target):
    # print(arr1)
    lst =[]
    n =len(arr1)
    for i in range(n):
        sum = target - arr1[i]

        if arr1[i] not in lst:
            lst.append(arr1[i])

        if sum in lst:
            print(arr1[i], sum)




# lst =1
arr = [1, 5, 7, -1, 5]
pairsum(arr, 6)