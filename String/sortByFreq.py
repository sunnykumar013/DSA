def sortFreq(str1):
    lst =list(str1)

    dict1={}
    res=""
    for i in range(len(lst)):
        if lst[i] in dict1:
            dict1[lst[i]] = 1 + dict1[lst[i]]

        else:
            dict1[lst[i]] = 1

    sortedDict = sorted(dict1,key = lambda x:dict1[x], reverse= False)

    for key in sortedDict:
        res += key*dict1[key]

    print(dict1)
    print(sortedDict)
    print(res)



str2 ="geeksforgeeksAAAAAAAAAAA"
print(sortFreq(str2))