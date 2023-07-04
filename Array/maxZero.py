def maxZero(str1):
    lst = list(str1)
    print(str1)

    c=0
    for i in range(len(lst)):
        if lst[i] =='0':
            c +=1


str1="assf00000ass00"
print(maxZero(str1))
