def pallendrome(s1):
    #2002
    i=0
    l =len(s1) -1
    c=0
    while(i<=l):
        if(s1[i] != s1[l]):
            c = c+1
            break
        i = i +1
        l= l - 1

    if(c==1):
        print("it is not pallendrome")

    else:
        print("it is pallendrome")



pallendrome("11223344556677889900000099887766554432211")

