def reversess(s1):
    s1 = list(s1)
    i =0;
    j = len(s1) -1

    while(i<=j):
        s1[i], s1[j] = s1[j], s1[i]

        i = i +1
        j = j-1
    s1 = "".join(s1)
    print(s1)

reversess("sunny")



