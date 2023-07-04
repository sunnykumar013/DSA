def sortString(str1):

    str2=""
    for i in range(ord('a'),ord('z')+1):
        for j in range(len(str1)):
            if(str1[j]== chr(i)):
                str2 += str1[j]

    return str2

print(sortString("bbccdefbbaa"))