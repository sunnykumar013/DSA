def reversess(s1):
    s1 = list(s1)
    i =0;
    j = len(s1) -1

    while(i<=j):
        if(s1[i] =='a' or s1[i] =='e' or s1[i] =='i' or s1[i] =='u' or s1[i] =='o' ):
            i +=1

        if (s1[j] == 'a' or s1[j] == 'e' or s1[j] == 'i' or s1[j] == 'u' or s1[j] == 'o'):
            j -= 1

        else:
            s1[i], s1[j] = s1[j], s1[i]

            i = i +1
            j = j-1

    s1 = "".join(s1)

    print(s1)

reversess("sunny")



