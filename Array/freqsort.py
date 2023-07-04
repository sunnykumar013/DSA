def fsort(arr):

    dict1 = {}

    for i in range(len(arr)):
        if arr[i] in dict1:
            dict1[arr[i]] = 1 + dict1[arr[i]]

        else:
            dict1[arr[i]] = 1

    liv =[]
    for key,value in dict1.items():
        liv.append(key)
    print(liv)


arr1 =[2, 3, 2, 4, 5, 12, 2, 3, 3, 3, 12]
fsort(arr1)