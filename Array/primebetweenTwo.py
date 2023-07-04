def betweenTwo(x,y):

    for i in range(x+1, y):
        c=0
        for j in range(2,i):
            if(i%j ==0):
                c=1
                break

        if(c==0):
            print(i)



print(betweenTwo(1,10))