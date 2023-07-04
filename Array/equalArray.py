def checkEqual(arr1,arr2):

    dict1={}

    for i in range(len(arr1)):
        if arr1[i] in dict1:
            dict1[arr1[i]]=1+ arr1[i]

        else:
            dict1[arr1[i]] = 1

    for i in range(len(arr2)):

        if arr2[i] not in dict1 or dict1[arr2[i]] ==0:

            return False

        else:
            dict1[arr2[i]] -= 1

    return True




arr3=[11,23,43,12]
arr4=[23,43,11,12]
print(checkEqual(arr3,arr4))