def repAndNonrep(s1):
    dict1 ={}
    l1=[]
    l2=[]
    # apple
    for i in range(len(s1)):
        if s1[i] in dict1:
            dict1[s1[i]] = dict1[s1[i]] +1



        else:
            dict1[s1[i]] = 1


    for key,value in dict1.items():

        if(value ==1):
            l1.append(key)

        else:
            l2.append(key)




    print(l1)
    print(l2)

repAndNonrep("ssssuuuuunny")